from django.urls import path
from . import views

urlpatterns = [
    path('bautizos/', views.bautizo_list, name='bautizos_list'),
    path('bautizos/<int:pk>/', views.bautizo_detail, name='bautizo_detail'),
    path('bautizos/<int:pk>/editar/', views.bautizo_update, name='bautizo_update'),
    path('bautizos/<int:pk>/eliminar/', views.bautizo_delete, name='bautizo_delete'),
    path('', views.sacramentos_home, name='sacramentos_home'),
    path('bautizos/crear/', views.bautizo_create, name='bautizo_create'),
    path('matrimonios/', views.matrimonios_list_view, name='matrimonios_list'),
    path('matrimonios/nuevo/', views.matrimonio_create_view, name='matrimonio_create'),
    path('sacramentos/', views.sacramentos_home, name='sacramentos_home'),

]
