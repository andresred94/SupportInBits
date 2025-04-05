from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('politicas/', views.politicas, name='politica-privacidad'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('cookies-policy/', views.cookies, name='politica-cookies'),
    path('test/', views.test, name='test')

]