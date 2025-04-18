from django import forms
from django.utils.text import slugify
from .models import Entrada, Categoria
from .models import Comentario

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'resumen', 'categoria', 'publicado', 'imagen_portada']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la entrada'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Contenido de la entrada...'
            }),
            'resumen': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Resumen breve (opcional)'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'publicado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'publicado': 'Publicar entrada'
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EntradaForm, self).__init__(*args, **kwargs)
        # Filtra categorías si es necesario
        self.fields['categoria'].queryset = Categoria.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.autor = self.user
        if not instance.slug:
            instance.slug = slugify(instance.titulo)
        if commit:
            instance.save()
            self.save_m2m()  # Para relaciones many-to-many si las hubiera
        return instance


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...'
            })
        }
        labels = {
            'contenido': ''
        }