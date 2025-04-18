from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from user.decorators import rol_requerido
from django.views.generic import ListView, DetailView, CreateView
from page.models import Page
from .models import Entrada, Seccion, Categoria
from django.contrib import messages
from .forms import EntradaForm, ComentarioForm

# Create your views here.

def home_blog(request):
    # Obtener los datos de la página desde Page
    pagina = Page.objects.get(id=6)  # Asegúrate de que el ID 6 corresponde a la página del blog
    
    # Obtener todas las entradas publicadas ordenadas por fecha (más recientes primero)
    entradas = Entrada.objects.filter(publicado=True).order_by('-fecha_publicacion')
    
    # Obtener todas las secciones con sus categorías para el sidebar
    secciones = Seccion.objects.prefetch_related('categorias').all()
    
    return render(
        request,
        'blog/home_blog.html',  # Asegúrate de que esta ruta es correcta
        context={
            'page': pagina,
            'entradas': entradas,
            'secciones': secciones
        }
    )

@rol_requerido('administrador')
def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            entrada = form.save()
            messages.success(request, f'Entrada "{entrada.titulo}" creada exitosamente!')
            return redirect(entrada.get_absolute_url())
    else:
        form = EntradaForm(user=request.user)
    
    return render(request, 'blog/crear_entrada.html', {'form': form})

""" @login_required
def crear_comentario(request, slug):
    entrada = get_object_or_404(Entrada, slug=slug)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.entrada = entrada
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentario agregado correctamente!')
    return redirect('detalle_entrada', slug=entrada.slug) """

@login_required
@require_POST
def crear_comentario(request, slug):
    entrada = get_object_or_404(Entrada, slug=slug)
    form = ComentarioForm(request.POST)
    
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.entrada = entrada
        comentario.autor = request.user
        
        # Si es moderador o admin, aprobar automáticamente
        if request.user.is_superuser or request.user.rol == 'moderador':
            comentario.aprobado = True
        
        comentario.save()
        messages.success(request, '¡Comentario enviado!')
    else:
        messages.error(request, 'Error al enviar el comentario')
    
    return redirect('detalle_entrada', slug=entrada.slug)


class ListaEntradas(ListView):
    model = Entrada
    template_name = 'blog/lista_entradas.html'
    context_object_name = 'entradas'
    paginate_by = 10
   

    def get_queryset(self):
        return Entrada.objects.filter(publicado=True).order_by('-fecha_publicacion')

class DetalleEntrada(DetailView):
    model = Entrada
    template_name = 'blog/detalle_entrada.html'
    context_object_name = 'entrada'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Configuración de la página
        context['page'] = Page.objects.get(id=6)
        context['page'].titulo = self.object.meta_titulo
        context['page'].m_descri = self.object.meta_descripcion
        context['page'].m_robots = self.object.meta_robots
        
        # Comentarios (solo aprobados o del usuario actual)
        # Obtener solo comentarios aprobados para el conteo
        comentarios_aprobados = self.object.comentarios.filter(aprobado=True)
        context['total_comentarios_aprobados'] = comentarios_aprobados.count()

        # Si el usuario está autenticado, incluir también sus comentarios no aprobados
        if self.request.user.is_authenticated:
            mis_comentarios = self.object.comentarios.filter(autor=self.request.user, aprobado=True)
            comentarios = comentarios_aprobados | mis_comentarios
        else:
            comentarios = comentarios_aprobados
        
        if self.request.user.is_staff:
            comentarios_no_aprobados = self.object.comentarios.filter(aprobado=False)
            context['comentarios_pendientes'] = comentarios_no_aprobados.order_by('fecha_creacion')
            
        context['comentarios'] = comentarios.order_by('fecha_creacion')
        context['form_comentario'] = ComentarioForm()  # Asegúrate de importar ComentarioForm
        
        # Pasar el usuario al contexto para usar en los métodos del modelo
        for comentario in context['comentarios']:
            comentario.current_user = self.request.user
        
        return context

class EntradasPorCategoria(ListView):
    template_name = 'blog/entradas_por_categoria.html'
    context_object_name = 'entradas'
    paginate_by = 10
    
    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs['slug_categoria'])
        return Entrada.objects.filter(categoria=self.categoria, publicado=True).order_by('-fecha_publicacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context

class EntradasPorSeccion(ListView):
    template_name = 'blog/entradas_por_seccion.html'
    context_object_name = 'entradas'
    paginate_by = 10
    
    def get_queryset(self):
        self.seccion = get_object_or_404(Seccion, slug=self.kwargs['slug_seccion'])
        categorias = self.seccion.categorias.all()
        return Entrada.objects.filter(categoria__in=categorias, publicado=True).order_by('-fecha_publicacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seccion'] = self.seccion
        return context