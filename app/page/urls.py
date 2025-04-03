from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quien_soy/', views.quien_soy, name='quien_soy'),
    path('politicas/', views.politicas, name='politica-privacidad'),
    path('about/', views.about, name='about'),
    # path('faq/', views.cookies, name='faq'),
    path('cookies-policy/', views.cookies, name='politica-cookies'),
    path('test/', views.test, name='test')

]