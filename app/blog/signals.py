from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Entrada

@receiver(pre_save, sender=Entrada)
def actualizar_pagina_desde_entrada(sender, instance, **kwargs):
    """
    Actualiza la página asociada cuando se cambia el título o el estado de publicación
    """
    if instance.pk and instance.pagina_id:  # Si ya existe
        original = Entrada.objects.get(pk=instance.pk)
        
        # Si cambió el título o el estado de publicación
        if original.titulo != instance.titulo or original.publicado != instance.publicado:
            instance.pagina.titulo = f"Support In Bits | {instance.titulo}"
            instance.pagina.m_descri = instance.resumen[:255] if instance.resumen else instance.titulo[:255]
            instance.pagina.m_robots = "index, follow" if instance.publicado else "noindex, nofollow"
            instance.pagina.save()