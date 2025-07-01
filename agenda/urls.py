from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda_home, name='agenda_home'),
    path('nuevo/', views.evento_nuevo, name='evento_nuevo'),
]
