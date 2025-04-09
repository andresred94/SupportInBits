from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
# Create your views here.

def home_blog(request):
    return render(
        request,
        'blog/home_blog.html'
    )

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'