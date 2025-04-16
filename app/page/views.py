from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Page
from user.forms import RegistroForm

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

def getAllPages(request):
    # Los values son los que aparecen en en el modelo
    paginas = Page.objects.all().values('id','titulo','m_descri','m_robots','m_handF','m_mobileOp')
    return JsonResponse(list(paginas), safe=False,  content_type="application/json")