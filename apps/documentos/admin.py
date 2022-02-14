
from django.contrib import admin

from .models import Estado, DetalleEstados, Documentacion

admin.site.register(Estado)
admin.site.register(DetalleEstados)
admin.site.register(Documentacion)

# Register your models here.
