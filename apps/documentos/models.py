
#from tabnanny import verbose
from django.db import models


class Estado(models.Model):
    descripcion = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Documentaciones"


class Documentacion(models.Model):
    nomenclatura = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.nomenclatura

    class Meta:
        verbose_name_plural = "Documentaciones"


class DetalleEstados(models.Model):
    fecha = models.DateField()
    documentacion = models.ForeignKey(Documentacion, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name_plural = "Detalle Estados"


# Create your models here.
