# sacramentos/views.py

from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BautizoForm
from .models import Bautizo

def bautizo_list(request):
    bautizos = Bautizo.objects.all().order_by('-fecha')
    return render(request, 'sacramentos/bautizo_list.html', {'bautizos': bautizos})

def bautizo_create(request):
    if request.method == 'POST':
        form = BautizoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bautizos_list')
    else:
        form = BautizoForm()
    return render(request, 'sacramentos/bautizo_form.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def sacramentos_home(request):
    return render(request, 'sacramentos/sacramentos_home.html')


@login_required
def bautizo_detail(request, pk):
    bautizo = get_object_or_404(Bautizo, pk=pk)
    return render(request, 'sacramentos/bautizo_detail.html', {'bautizo': bautizo})

@login_required
def bautizo_update(request, pk):
    bautizo = get_object_or_404(Bautizo, pk=pk)
    if request.method == 'POST':
        form = BautizoForm(request.POST, instance=bautizo)
        if form.is_valid():
            form.save()
            return redirect('bautizos_list')
    else:
        form = BautizoForm(instance=bautizo)
    return render(request, 'sacramentos/bautizo_form.html', {'form': form, 'form_title': 'Editar Bautizo'})


@login_required
def bautizo_delete(request, pk):
    bautizo = get_object_or_404(Bautizo, pk=pk)
    if request.method == 'POST':
        bautizo.delete()
        return redirect('bautizos_list')
    return render(request, 'sacramentos/bautizo_confirm_delete.html', {'bautizo': bautizo})


from django.shortcuts import render, redirect
from .models import Matrimonio
from .forms import MatrimonioForm

def matrimonio_create_view(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matrimonios_list')
    else:
        form = MatrimonioForm()
    return render(request, 'sacramentos/matrimonio_form.html', {'form': form, 'form_title': 'Registrar Matrimonio'})


from django.shortcuts import render
from .models import Matrimonio

def matrimonios_list_view(request):
    matrimonios = Matrimonio.objects.all().order_by('-fecha')
    return render(request, 'sacramentos/matrimonios_list.html', {'matrimonios': matrimonios})


from django.shortcuts import render, redirect
from .models import Matrimonio
from .forms import MatrimonioForm

def matrimonios_list(request):
    matrimonios = Matrimonio.objects.all().order_by('-fecha')
    return render(request, 'sacramentos/matrimonios_list.html', {'matrimonios': matrimonios})

def matrimonio_create(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matrimonios_list')
    else:
        form = MatrimonioForm()
    return render(request, 'sacramentos/matrimonio_form.html', {'form': form})
