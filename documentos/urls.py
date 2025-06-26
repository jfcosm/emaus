from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('crear/', views.document_create, name='document_create'),
]
