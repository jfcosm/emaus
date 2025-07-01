from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import landing_root_view, landing_always_view, home
from . import views
from .views import registro_provisional, presentacion_emaus
from django.urls import path
from .views import CustomLoginView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('documentos/', include('documentos.urls')),
    path('sacramentos/', include('sacramentos.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('bienvenida/', landing_always_view, name='landing'),       # Siempre muestra landing
    path('', landing_root_view, name='root_landing'),               # Solo muestra landing si NO estás logueado
    path('inicio/', home, name='home'),                             # Dashboard
    path('redirigir/sacramentos/', views.sacramentos_redirect, name='sacramentos_redirect'),
    path('redirigir/documentos/', views.documentos_redirect, name='documentos_redirect'),
    path('redirigir/agenda/', views.agenda_redirect, name='agenda_redirect'),
    path('presentacion/', views.presentacion_emaus, name='presentacion_emaus'),
    path('agenda/', include('agenda.urls')),
    path('registro/', registro_provisional, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),

]
