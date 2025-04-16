from django.urls import path
from . import views

urlpatterns = [
    path('registrate/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/panel/', views.panel_administrador, name='panel_administrador'),
    path('admin/comentarios/', views.gestion_comentarios, name='gestion_comentarios'),
    
    #path('admin/usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    #path('admin/entradas/', views.gestion_entradas, name='gestion_entradas'),
    # Entradas
    # path('entradas/', views.EntradaListView.as_view(), name='lista_entradas'),
    # path('entradas/<slug:slug>/', views.EntradaDetailView.as_view(), name='detalle_entrada'),
    
    # Comentarios
    # path('entradas/<slug:slug>/comentar/', views.crear_comentario, name='crear_comentario'),
    # path('comentarios/', views.gestion_comentarios, name='gestion_comentarios'),
    # path('comentarios/<int:pk>/<str:accion>/', views.moderar_comentario, name='moderar_comentario'),
]