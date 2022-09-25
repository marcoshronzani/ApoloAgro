from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes, name = 'clientes'),
    path('categorias/', views.categorias, name = 'categorias'),
    path('cria_categoria', views.cria_categoria, name = 'cria_categoria'),
    path('valida_categoria', views.valida_categoria, name = 'valida_categoria'),
    path('edita_categoria/<int:id>', views.edita_categoria, name = 'edita_categoria'),
]