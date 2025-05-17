"""supportinbits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import buscar_entradas_ajax

urlpatterns = [
    # path('admin/', perfil_admin, name="perfil_admin"),
    # path('admin/', include('user.urls')),
    path('', include('page.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('accounts/', include('allauth.urls')),  # rutas de allauth
    path('blog/', include('blog.urls')),
    path('identificate/', include('user.urls')),
    path('mi-perfil/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('buscar/ajax/', buscar_entradas_ajax, name='buscar_entradas_ajax'),
]
