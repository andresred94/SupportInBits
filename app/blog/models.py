from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    content = HTMLField()