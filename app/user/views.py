from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .decorators import rol_requerido
from django.contrib import messages
from blog.models import Entrada, Comentario, Seccion, Categoria
from .forms import RegistroForm, LoginForm
from .models import Usuario
from page.models import Page
""" from django.urls import reverse_lazy """
""" from django.contrib.auth.forms import AuthenticationForm """
""" from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView """
""" from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin """


# Vista de registro

def registro(request):
    pagina = Page.objects.get(id=9)
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Iniciar sesión automáticamente después del registro
            login(request,user)
            
            # Redirección basada en el rol
            if user.is_superuser:
                return redirect('perfil_admin')
            elif user.rol == 'moderador':
                return redirect('tests')
            else:
                return redirect('perfil_registrado')
    else:
        form = RegistroForm()
    
    # Manejar el parámetro 'next' para redirección post-registro
    next_param = request.GET.get('next', '')
    
    return render(
        request,
        'user/registro.html', 
        context={
        'form': form,
        'next': next_param,
        'page': pagina,
    })



def user_login(request):
    pagina = Page.objects.get(id=8)
    
    # Eliminar la verificación inicial de is_authenticated
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {username}!')
                
                # Redirección basada en el rol
                if user.is_superuser:
                    return redirect('perfil_admin')
                elif user.rol == 'moderador':
                    return redirect('tests')
                else:
                    return redirect('perfil_registrado')
        else:
            # Mostrar errores específicos del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        'user/login.html', {
        'form': form,
        'page': pagina,
    })

def perfil_registrado(request):
    pagina = Page.objects.get(id=10)
    return render(
            request,
            'user/perfil_registrado.html', {
            'page': pagina,
        })

@rol_requerido('administrador')
def perfil_admin(request):
    pagina = Page.objects.get(id=10)
    return render(
            request,
            'user/perfil_admin.html', {
            'page': pagina,
        })
# Vista de logout
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('home')

# Vista para crear comentario
# @login_required
""" def crear_comentario(request, slug):
    entrada = get_object_or_404(Entrada, slug=slug)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.entrada = entrada
            comentario.autor = request.user
            # Si es moderador o admin, aprobar automáticamente
            if request.user.es_moderador:
                comentario.aprobado = True
            comentario.save()
            messages.success(request, 'Comentario agregado!')
            return redirect('detalle_entrada', slug=entrada.slug)
    return redirect('detalle_entrada', slug=entrada.slug)
 """
# Vista para gestionar comentarios (solo moderadores/admins)
@login_required
def gestion_comentarios(request):
    if not request.user.es_moderador:
        return redirect('home')
    
    comentarios = Comentario.objects.all().order_by('-fecha_creacion')
    if not request.user.es_administrador:
        comentarios = comentarios.filter(entrada__autor=request.user)
    
    return render(request, 'blog/gestion_comentarios.html', {
        'comentarios': comentarios
    })

# Vista para aprobar/rechazar comentarios
@login_required
def moderar_comentario(request, pk, accion):
    if not request.user.es_moderador:
        return redirect('home')
    
    comentario = get_object_or_404(Comentario, pk=pk)
    
    if accion == 'aprobar':
        comentario.aprobado = True
        comentario.save()
        messages.success(request, 'Comentario aprobado.')
    elif accion == 'rechazar':
        comentario.delete()
        messages.success(request, 'Comentario eliminado.')
    
    return redirect('gestion_comentarios')

def is_superuser(user):
    return user.is_superuser or (hasattr(user, 'rol') and user.rol == 'administrador')

@user_passes_test(is_superuser, login_url='/identificate/')
def panel_administrador(request):
    # Obtener todos los objetos que puede gestionar
    usuarios = Usuario.objects.all().order_by('-date_joined')
    entradas = Entrada.objects.all().order_by('-fecha_publicacion')
    comentarios = Comentario.objects.all().order_by('-fecha_creacion')
    
    # Estadísticas
    total_usuarios = usuarios.count()
    total_entradas = entradas.count()
    total_comentarios = comentarios.count()
    
    context = {
        'usuarios': usuarios[:5],  # Últimos 5 registrados
        'entradas': entradas[:5],  # Últimas 5 entradas
        'comentarios': comentarios[:5],  # Últimos 5 comentarios
        'total_usuarios': total_usuarios,
        'total_entradas': total_entradas,
        'total_comentarios': total_comentarios,
    }
    
    return render(request, 'admin/panel_administrador.html', context)