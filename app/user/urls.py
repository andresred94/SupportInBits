from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    # ... otras URLs ...
]