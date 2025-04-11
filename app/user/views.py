from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear el perfil
            Profile.objects.create(
                user=user,
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                rol='BLOGGER'  # Rol por defecto
            )
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'blog/registro.html', {'form': form})