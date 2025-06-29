from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def document_view(request, pk):
    doc = get_object_or_404(Documento, pk=pk)
    return render(request, 'documentos/view.html', {'doc': doc})


@login_required
def document_edit(request, pk):
    doc = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentoForm(instance=doc)
    return render(request, 'documentos/form.html', {'form': form})


@login_required
def document_delete(request, pk):
    doc = get_object_or_404(Documento, pk=pk)
    if request.method == 'POST':
        doc.delete()
        return redirect('document_list')
    return render(request, 'documentos/confirm_delete.html', {'doc': doc})
