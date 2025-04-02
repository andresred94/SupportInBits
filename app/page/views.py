from django.shortcuts import render
from .models import Page
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
        'quien_soy.html',
        # context={'pagina': page}
    )