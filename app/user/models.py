from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('BLOGGER', 'Blogger'),
        ('MODERADOR', 'Moderador'),
        ('ADMIN', 'Administrador'),
    )
    
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rol = models.CharField(max_length=10, choices=ROLES, default='BLOGGER')
    
    # Si quieres que el email sea único y requerido
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.username})"
    
    @property
    def es_blogger(self):
        return self.rol == 'BLOGGER'
    
    @property
    def es_moderador(self):
        return self.rol == 'MODERADOR'
    
    @property
    def es_admin(self):
        return self.rol == 'ADMIN'