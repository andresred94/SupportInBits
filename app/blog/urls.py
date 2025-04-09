from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', views.home_blog, name='home_blog'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
