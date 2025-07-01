from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'dashboard.html')


from django.shortcuts import render, redirect

def landing_root_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige solo desde la raíz
    return render(request, 'landing.html')

def landing_always_view(request):
    return render(request, 'landing.html')  # No redirige nunca



from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def sacramentos_redirect(request):
    if request.user.is_authenticated:
        return redirect('sacramentos_home')  # ← nombre correcto
    else:
        return redirect('presentacion_emaus')


def documentos_redirect(request):
    if request.user.is_authenticated:
        return redirect('document_list')  # ✅ nombre correcto
    else:
        return redirect('presentacion_emaus')

def agenda_redirect(request):
    if request.user.is_authenticated:
        return redirect('agenda_home')
    else:
        return redirect('presentacion_emaus')



def presentacion_emaus(request):
    return render(request, 'landing/presentacion_emaus.html')

from django.shortcuts import render

def registro_provisional(request):
    return render(request, 'landing/registro_provisional.html')


from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm


