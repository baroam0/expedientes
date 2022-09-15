
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from .models import Documento


class DocumentoView(View):
    #filter_val = self.request.GET.get('filter', 'give-default-value')
    def get(self, request):
        documentos = Documento.objects.all()

        items_documento = list()

        for documento in documentos:
            items_documento.append({
                'nomenclatura': documento.nomenclatura.upper(),
                'descripcion': documento.descripcion.upper(),
            })

        data = {
            'documents': items_documento
        }

        return JsonResponse(data)


# Create your views here.
