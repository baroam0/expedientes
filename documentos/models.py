
from django.db import models

from zonas.models import Barrio


class Estado(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Estado, self).save(*args, **kwargs)

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
    
    def save(self, *args, **kwargs):
        self.nomenclatura = self.nomenclatura.upper()
        self.descripcion = self.descripcion.upper()
        super(Documento, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Documentos"


# Create your models here.
