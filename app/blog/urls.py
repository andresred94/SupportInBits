from django.urls import path
from . import views
from .views import DetalleEntrada, EntradasPorCategoria, EntradasPorSeccion


urlpatterns = [
    path('', views.home_blog, name='home_blog'),
    # path('crear/', registro, name='crear_entrada'),
    # path('', ListaEntradas.as_view(), name='lista_entradas'),
    path('<slug:slug>/', DetalleEntrada.as_view(), name='detalle_entrada'),
    path('categoria/<slug:slug_categoria>/', EntradasPorCategoria.as_view(), name='entradas_por_categoria'),
    path('seccion/<slug:slug_seccion>/', EntradasPorSeccion.as_view(), name='entradas_por_seccion'),
]
