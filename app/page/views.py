from django.shortcuts import render
from .models import Page
# Create your views here.

def home(request):
    pagina = Page.objects.get(id=1)
    return render(
        request,
        'home.html',
        context={'page': pagina}  # Enviar la lista de objetos a la plantilla
    )
def cookies(request):
    pagina = Page.objects.get(id=2)
    return render(
        request,
        'cookies.html',
        context={'page': pagina}
    )
def about(request):
    pagina = Page.objects.get(id=3) 
    return render(
        request,
        'about.html',
        context={'page': pagina}
    )
def politicas(request):
    pagina = Page.objects.get(id=4)
    return render(
        request,
        'politicas_privacidad.html',
        context={'page': pagina}
    )

def faq(request): 
    pagina = Page.objects.get(id=5)
    return render(
        request,
        'faq.html',
        context={'page': pagina}
    )

def test(request):
    return render(
        request,
        'test.html',
    )