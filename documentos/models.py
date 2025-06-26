from django.db import models
from ckeditor.fields import RichTextField


class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo
