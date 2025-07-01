from django.shortcuts import render, redirect
from .models import EventoParroquial
from .forms import EventoParroquialForm
from django.contrib.auth.decorators import login_required

import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import EventoParroquial

@login_required
def agenda_home(request):
    eventos = EventoParroquial.objects.all()

    eventos_serializados = [
        {
            "title": evento.titulo,
            "start": f"{evento.fecha}T{evento.hora}",
            "description": evento.descripcion or "",
        }
        for evento in eventos
    ]

    eventos_json = json.dumps(eventos_serializados)

    return render(request, 'agenda/agenda_home.html', {
        'eventos_json': eventos_json  # clave que se usa en el template
    })

@login_required
def evento_nuevo(request):
    if request.method == 'POST':
        form = EventoParroquialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda_home')
    else:
        form = EventoParroquialForm()
    return render(request, 'agenda/evento_form.html', {'form': form})
