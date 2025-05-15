from django.urls import path, include
from .views import DetalleEntrada, EntradasPorCategoria, EntradasPorSeccion, ListaEntradasView, EditarEntradaView, EliminarEntradaView
from .views import crear_entrada, crear_comentario, home_blog

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('entradas-admin/', ListaEntradasView.as_view(), name='lista_entradas_admin'),
    path('entradas/nueva/', crear_entrada, name='crear_entrada'),
    path('entradas/editar/<slug:slug>/', EditarEntradaView.as_view(), name='editar_entrada'),
    path('entradas/<slug:slug>/comentar/', crear_comentario, name='crear_comentario'),
    path('entradas/eliminar/<slug:slug>/', EliminarEntradaView.as_view(), name='eliminar_entrada'),
    path('entrada/<slug:slug>/', DetalleEntrada.as_view(), name='detalle_entrada'),
    path('<slug:slug_seccion>/<slug:slug_categoria>/', EntradasPorCategoria.as_view(), name='entradas_por_categoria'),
    path('<slug:slug_seccion>/', EntradasPorSeccion.as_view(), name='entradas_por_seccion'),
    path('tinymce/', include('tinymce.urls')),
    #path('categoria/<slug:slug_categoria>/', EntradasPorCategoria.as_view(), name='entradas_por_categoria'),
    # path('entradas/comentario/', crear_entrada, name='crear_entrada'),
]
