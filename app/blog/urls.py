from django.urls import path
from .views import DetalleEntrada, EntradasPorCategoria, EntradasPorSeccion
from .views import crear_entrada, crear_comentario, home_blog

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('entradas/nueva/', crear_entrada, name='crear_entrada'),
    path('entradas/comentario/', crear_entrada, name='crear_entrada'),
    path('entradas/<slug:slug>/comentar/', crear_comentario, name='crear_comentario'),
    path('<slug:slug>/', DetalleEntrada.as_view(), name='detalle_entrada'),
    path('categoria/<slug:slug_categoria>/', EntradasPorCategoria.as_view(), name='entradas_por_categoria'),
    path('seccion/<slug:slug_seccion>/', EntradasPorSeccion.as_view(), name='entradas_por_seccion'),
]
