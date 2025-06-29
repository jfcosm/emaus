from django.urls import path
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('crear/', views.document_create, name='document_create'),
    path('<int:pk>/ver/', views.document_view, name='document_view'),
    path('<int:pk>/editar/', views.document_edit, name='document_edit'),
    path('<int:pk>/eliminar/', views.document_delete, name='document_delete'),
]
