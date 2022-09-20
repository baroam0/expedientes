

from django import forms

from .models import Documento, Estado
from zonas.models import Barrio


class DocumentoForm(forms.ModelForm):    

    nomenclatura = forms.CharField(label="Nomenclatura", required=True)
    descripcion = forms.CharField(label="Descripcion", required=True)
    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all().order_by('descripcion'), 
        label="Estado",
        required=True
    )
    fechaestado = forms.DateField(
        label="Fecha Estado", required=False)
    
    barrio = forms.ModelMultipleChoiceField(
        widget = forms.SelectMultiple,
        queryset = Barrio.objects.all().order_by('descripcion')
    )

    referenciadescriptiva = forms.CharField(label="Referencia Auxiliar", required=False)

    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            print(field)
            if field != 'barrio':
                self.fields[field].widget.attrs.update({
                    'class': 'pure-input-1'
                })

    class Meta:
        model = Documento
        fields = ['nomenclatura', 'descripcion', 'estado', 'fechaestado',
                  'barrio' ]

