# sacramentos/models.py

from django.db import models

class Bautizo(models.Model):
    rut = models.CharField(max_length=12, help_text="Ej: 12345678-9")
    nombres_bautizado = models.CharField(max_length=100)
    apellidos_bautizado = models.CharField(max_length=100)
    fecha = models.DateField()
    celebrante = models.CharField(max_length=100)
    iglesia = models.CharField(max_length=100)
    nombre_padre = models.CharField(max_length=100)
    nombre_madre = models.CharField(max_length=100)
    nombre_padrino = models.CharField(max_length=100)  # nuevo
    nombre_madrina = models.CharField(max_length=100)  # nuevo
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Bautizo de {self.nombres_bautizado} {self.apellidos_bautizado} ({self.rut})"



from django.db import models

class Matrimonio(models.Model):
    nombres_novio = models.CharField(max_length=100)
    apellidos_novio = models.CharField(max_length=100)
    nombres_novia = models.CharField(max_length=100)
    apellidos_novia = models.CharField(max_length=100)
    fecha = models.DateField()
    celebrante = models.CharField(max_length=100)
    iglesia = models.CharField(max_length=100)
    nombre_padrino_novio = models.CharField(max_length=100, blank=True, null=True)
    nombre_madrina_novio = models.CharField(max_length=100, blank=True, null=True)
    nombre_padrino_novia = models.CharField(max_length=100, blank=True, null=True)
    nombre_madrina_novia = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombres_novio} y {self.nombres_novia} ({self.fecha})"
