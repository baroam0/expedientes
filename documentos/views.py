

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Documento
from .forms import DocumentoForm


def documentolistado(request):
    if "param" in request.GET:
        parametro = request.GET.get("param")
        consulta = Documento.objects.filter(
            Q(nomenclatura__icontains=parametro) |
            Q(descripcion__contains=parametro) 
        ).order_by('nomenclatura')
    else:
        consulta = Documento.objects.all().order_by('estado')

    paginador = Paginator(consulta, 20)

    if "page" in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    resultados = paginador.get_page(page)
    return render(request, 'documentos/documento_list.html', {'resultados': resultados})


def documentonuevo(request):
    if request.POST:
        form = DocumentoForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "SE HAN GUARDADO LOS DATOS")
            return redirect('/documentolistado/')
        else:
            return render(
                request,
                'pacientes/paciente_nuevo.html',
                {
                    "form": form,
                })
    else:
        form = DocumentoForm()
        return render(
            request,
            'documentos/documento_nuevo.html',
            {
                "form": form,
            }
        )


def documentoeditar(request, pk):
    consulta = Documento.objects.get(pk=pk)
    
    if request.POST:
        form = DocumentoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, "SE HA MOFICICADO EL EXPEDIENTE")
            return redirect('/documentos/listado')
        else:
            return render(request, "documentos/documento_nuevo.html", {"form": form})
    else:
        form = DocumentoForm(instance=consulta)
        return render(
            request,
            'documentos/documento_nuevo.html',
            {
                "form": form,
            }
        )


# Create your views here.
