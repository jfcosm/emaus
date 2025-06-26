from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SacramentoForm
from .models import Sacramento


@login_required
def sacramento_list(request):
    registros = Sacramento.objects.all()
    return render(request, 'sacramentos/list.html', {'registros': registros})


@login_required
def sacramento_create(request):
    if request.method == 'POST':
        form = SacramentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sacramento_list')
    else:
        form = SacramentoForm()
    return render(request, 'sacramentos/form.html', {'form': form})
