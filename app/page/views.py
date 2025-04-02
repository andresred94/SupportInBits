from django.shortcuts import render
# from .models import Page
# Create your views here.

def home(request):
    return render(
        request,
        'home.html',
        # context={'page': page}  # Enviar la lista de objetos a la plantilla
    )
def quien_soy(request):
    return render(
        request,
        'about.html',
        # context={'pagina': page}
    )
def politicas(request): 
    return render(
        request,
        'politicas_privacidad.html',
    )

def about(request): 
    return render(
        request,
        'about.html',
    )

def faq(request): 
    return render(
        request,
        'faq.html',
    )
def cookies(request): 
    return render(
        request,
        'cookies.html',
    )

def test(request):
    return render(
        request,
        'test.html',
    )