
from django.db import models


class Barrio(models.Model):
    descripcion = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Barrios"


# Create your models here.
