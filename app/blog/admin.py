from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user.models import Usuario

# Register your models here.
from .models import Seccion, Categoria, Entrada

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'publicado')
    list_filter = ('categoria', 'publicado')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    exclude = ('pagina',)  # Oculta el campo página en el formulario admin
    
    def save_model(self, request, obj, form, change):
        # Guarda el modelo y asegura que se ejecute el save() personalizado
        super().save_model(request, obj, form, change)

class ProfileInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Perfiles'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_rol')
    
    def get_rol(self, instance):
        return instance.profile.rol
    get_rol.short_description = 'Rol'

# admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Entrada, EntradaAdmin)