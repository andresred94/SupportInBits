from django.db import models

# Create your models here.

class Page (models.Model):
    titulo = models.CharField(max_length=255)
    descri = models.CharField(max_length=255)
    estilo = models.CharField(max_length=255, null=True, blank=True)