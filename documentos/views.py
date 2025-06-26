from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DocumentoForm
from .models import Documento


@login_required
def document_list(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/list.html', {'documentos': documentos})


@login_required
def document_create(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentoForm()
    return render(request, 'documentos/form.html', {'form': form})
