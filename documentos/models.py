
from django.db import models

from zonas.models import Barrio


class Estado(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Estados"


class Documento(models.Model):
    nomenclatura = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    descripcion = models.CharField(
        max_length=500, blank=False, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fechaestado = models.DateField(null=True)
    barrio = models.ManyToManyField(Barrio)
    referenciadescriptiva = models.CharField(
        max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nomenclatura.upper()

    class Meta:
        verbose_name_plural = "Documentos"


# Create your models here.
