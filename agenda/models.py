from django.db import models

class EventoParroquial(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha} {self.hora}"
