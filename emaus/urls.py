from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('documentos/', include('documentos.urls')),
    path('sacramentos/', include('sacramentos.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home'),
    path('', views.home, name='dashboard'),
    path('', include('sacramentos.urls')),

]
