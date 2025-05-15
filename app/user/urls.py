from django.urls import path
from .decorators import rol_requerido
from . import views
from page.views import acceso_denegado
handler403 = acceso_denegado  # Asigna tu vista personalizada
urlpatterns = [
    path('registrate/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.perfil_registrado, name='perfil_registrado'),
    # path('admin', rol_requerido('administrador')(views.perfil_admin), name='perfil_admin'),
    path('admin', views.perfil_admin, name='perfil_admin'),
    path('admin/comentarios/', views.gestion_comentarios, name='gestion_comentarios'),
    
    # path('admin/usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    # path('admin/entradas/', views.gestion_entradas, name='gestion_entradas'),
    # Entradas
    # path('entradas/', views.EntradaListView.as_view(), name='lista_entradas'),
    # path('entradas/<slug:slug>/', views.EntradaDetailView.as_view(), name='detalle_entrada'),
    
    # Comentarios
    # path('entradas/<slug:slug>/comentar/', views.crear_comentario, name='crear_comentario'),
    # path('comentarios/', views.gestion_comentarios, name='gestion_comentarios'),
    # path('comentarios/<int:pk>/<str:accion>/', views.moderar_comentario, name='moderar_comentario'),
]