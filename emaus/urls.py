from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import landing_root_view, landing_always_view, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('documentos/', include('documentos.urls')),
    path('sacramentos/', include('sacramentos.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('bienvenida/', landing_always_view, name='landing'),       # Siempre muestra landing
    path('', landing_root_view, name='root_landing'),               # Solo muestra landing si NO estás logueado
    path('inicio/', home, name='home'),                             # Dashboard
]
