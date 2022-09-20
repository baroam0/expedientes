

from rest_framework.viewsets import ModelViewSet

from .models import Documento
from .serializers import DocumentoSerializer


class DocumentoViewSet(ModelViewSet):
    queryset = Documento.objects.all().order_by('pk')
    serializer_class = DocumentoSerializer


# Create your views here.
