from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from user.models import Usuario
from user.forms import RegistroForm
from page.models import Page
from .models import Entrada, Seccion, Categoria
from .decorators import rol_requerido
from django.contrib.auth import login, logout
from django.contrib import messages
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



""" def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear el perfil
            Usuario.objects.create(
                user=user,
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                rol='BLOGGER'  # Rol por defecto
            )
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'blog/registro.html', {'form': form})
 """


class CrearEntradaView(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['titulo', 'contenido', 'resumen', 'categoria', 'imagen_portada']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.profile.es_blogger() or self.request.user.profile.es_admin()



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
        # Obtenemos la página del blog (ID 6) como base
        context['page'] = Page.objects.get(id=6)
        # Sobrescribimos los campos que necesitamos
        context['page'].titulo = self.object.meta_titulo
        context['page'].m_descri = self.object.meta_descripcion
        context['page'].m_robots = self.object.meta_robots
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