

from rest_framework import serializers

from .models import Documento, Estado


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"


class DocumentoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Documento
        fields = ['id', 'nomenclatura', 'descripcion', 'estado']
