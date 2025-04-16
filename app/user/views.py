from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Entrada, Comentario, Seccion, Categoria
from .forms import RegistroForm, LoginForm
from page.models import Page
# Vista de inicio


# Vista de registro

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Iniciar sesión automáticamente después del registro
            login(request,user)
            
            messages.success(request, 
                f'¡Registro exitoso! Bienvenido {user.username}. '
                'Ahora puedes comenzar a comentar en las entradas.'
            )
            

            # Redirigir al home o a la página que venía en 'next'
            next_url = request.POST.get('next', '')
            return redirect(next_url if next_url else 'home')
    else:
        form = RegistroForm()
    
    # Manejar el parámetro 'next' para redirección post-registro
    next_param = request.GET.get('next', '')
    
    return render(
        request,
        'user/registro.html', 
        context={
        'form': form,
        'next': next_param
    })

def login_view(request):
    pagina = Page.objects.get(id=8)
    if request.user.is_authenticated:
        # El usuario está logueado
        print(f"Usuario autenticado: {request.user.username}")
    else:
        # El usuario no está logueado
        print("Usuario no autenticado")
        
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(
        request, 
        'user/login.html', 
        context={
            'form': form,
            'page':pagina
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