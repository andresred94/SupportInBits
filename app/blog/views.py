from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q, Count
from django.contrib import messages
from page.models import Page
from user.decorators import rol_requerido
from .models import Entrada, Seccion, Categoria
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
        #form = EntradaForm(request.POST, request.FILES, user=request.user)
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            entrada = form.save()
            messages.success(request, f'Entrada "{entrada.titulo}" creada exitosamente!')
            return redirect(entrada.get_absolute_url())
    else:
        # form = EntradaForm(user=request.user)
        form = EntradaForm()
    
    return render(request, 'blog/crear_entrada.html', {'form': form})

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




@method_decorator(rol_requerido('administrador'), name='dispatch')
class ListaEntradasView(ListView):
    model = Entrada
    template_name = 'blog/lista_entradas_admin.html'
    context_object_name = 'entradas'
    paginate_by = 10  # Opcional para paginación del lado del servidor

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '').strip()
        
        if search_query:
            queryset = queryset.filter(
                Q(titulo__icontains=search_query) |
                Q(contenido__icontains=search_query) |
                Q(resumen__icontains=search_query) |
                Q(categoria__nombre__icontains=search_query)
            ).distinct()
        
        return queryset.order_by('-fecha_publicacion')

@method_decorator(rol_requerido('administrador'), name='dispatch')
class EliminarEntradaView(DeleteView):
    model = Entrada
    template_name = 'blog/confirmar_eliminar_entrada.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('lista_entradas_admin')
    roles_requeridos = ['administrador']  # Solo administradores pueden eliminar

    def delete(self, request, *args, **kwargs):
        entrada = self.get_object()
        messages.success(request, f'Entrada "{entrada.titulo}" eliminada correctamente')
        return super().delete(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        # Verificación adicional: solo el autor o superusuario puede eliminar
        entrada = self.get_object()
        if not (request.user == entrada.autor or request.user.is_superuser):
            messages.error(request, "No tienes permiso para eliminar esta entrada")
            return redirect(entrada.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)
         
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

class EditarEntradaView(UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog/editar_entrada.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('lista_entradas_admin')
    roles_requeridos = ['administrador', 'editor']  # Requiere rol admin o editor

    def form_valid(self, form):
        messages.success(self.request, f'Entrada "{form.instance.titulo}" actualizada correctamente')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(id=6)  # Ajusta el ID según tu configuración
        return context

class EntradasPorCategoria(ListView):
    model = Entrada
    template_name = 'blog/entradas_por_categoria.html'
    context_object_name = 'entradas'

    def get_queryset(self):
        slug_seccion = self.kwargs['slug_seccion']
        slug_categoria = self.kwargs['slug_categoria']
        return Entrada.objects.filter(
            categoria__slug=slug_categoria,
            categoria__seccion__slug=slug_seccion,
            publicado=True
        )

class EntradasPorSeccion(ListView):
    template_name = 'blog/entradas_por_seccion.html'
    context_object_name = 'entradas'
    paginate_by = 10
    
    def get_queryset(self):
        self.seccion = get_object_or_404(Seccion, slug=self.kwargs['slug_seccion'])
        categorias = self.seccion.categorias.all()
        return Entrada.objects.filter(
            categoria__in=categorias, 
            publicado=True
        ).select_related('categoria', 'autor').order_by('-fecha_publicacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seccion'] = self.seccion
        # Categorías de la sección con conteo de entradas publicadas
        context['categorias'] = self.seccion.categorias.annotate(
            num_entradas=Count(  # Usa Count directamente (sin models.)
                'entradas',
                filter=Q(entradas__publicado=True)  # Usa Q directamente
            )
        )
        return context