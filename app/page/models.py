from django.db import models

# Create your models here.

class Page (models.Model):
    titulo = models.CharField(max_length=255,null=False)
    m_descri = models.CharField(max_length=255,null=False)
    m_robots = models.CharField(max_length=255,null=False)
    m_handF = models.CharField(max_length=255, null=True)
    m_mobileOp = models.CharField(max_length=255, null=True)
    # estilo = models.CharField(max_length=255, null=True, blank=True)