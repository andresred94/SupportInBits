from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_blog, name='home_blog'),
    path('create/', views.create_post, name='create_post'),

]
