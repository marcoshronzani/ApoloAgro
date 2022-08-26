from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes, name = 'clientes'),
    path('categorias/', views.categorias, name = 'categorias')
]