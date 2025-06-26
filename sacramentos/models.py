from django.db import models


class Sacramento(models.Model):
    BAUTIZO = 'bautizo'
    COMUNION = 'comunion'
    CONFIRMACION = 'confirmacion'
    MATRIMONIO = 'matrimonio'
    DEFUNCION = 'defuncion'
    TIPOS = [
        (BAUTIZO, 'Bautizo'),
        (COMUNION, 'Primera Comunión'),
        (CONFIRMACION, 'Confirmación'),
        (MATRIMONIO, 'Matrimonio'),
        (DEFUNCION, 'Defunción'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha = models.DateField()
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Sacramento'
        verbose_name_plural = 'Sacramentos'

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.get_tipo_display()}"
