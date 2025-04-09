from django.shortcuts import render, redirect
from .forms import PostForm
from page.models import Page
# Create your views here.

def home_blog(request):
    pagina = Page.objects.get(id=6)
    return render(
        request,
        'blog/home_blog.html',
        context={'page': pagina}
    )

def create_post(request):
    form = PostForm(request.POST or None)

    page = Page.objects.get(id=7)  # o usa un slug si prefieres hacerlo más flexible

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('post_success')

    return render(
        request,
        'blog/create_post.html',
        {
            'form': form,
            'page': page
        }
    )