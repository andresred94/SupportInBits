from django import forms
from .models import Entrada, Categoria
from django.core.exceptions import ValidationError

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'resumen', 'categoria', 'imagen_portada']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'tinymce-editor'}),
            'resumen': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.all()
        self.fields['contenido'].required = True