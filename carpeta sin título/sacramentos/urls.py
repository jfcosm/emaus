from django.urls import path
from . import views

urlpatterns = [
    path('', views.sacramento_list, name='sacramento_list'),
    path('crear/', views.sacramento_create, name='sacramento_create'),
]
