from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quien_soy/', views.quien_soy, name='quien_soy'),
    path('cookies/', views.cookies, name='cookies'),
    path('test/', views.test, name='test')

]