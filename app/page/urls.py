from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('politicas-de-privacidad/', views.politicas, name='politica-privacidad'),
    path('quien-soy/', views.about, name='about'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('politica-de-cookies/', views.cookies, name='politica-cookies'),
    path('test/', views.test, name='tests')

]