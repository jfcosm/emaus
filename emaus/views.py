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
