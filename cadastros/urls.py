from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes, name = 'clientes'),
    path('categorias/', views.categorias, name = 'categorias'),
    path('cria_categoria', views.criar_categoria, name = 'cria_categoria'),
    path('edita_categoria/<int:id>', views.edita_categoria, name = 'edita_categoria'),
    path('exluir_categoria/<int:id>', views.excluir_categoria, name='excluir_categoria'),
    path('produtos/', views.produtos, name='produtos'),
    path('cria_produto/', views.cria_produto, name='cria_produto'),
    path('cria_servico', views.cria_servico, name='cria_servico'),
    path('servicos', views.servicos, name='servicos'),
    path('valida_produto', views.valida_produto, name='valida_produto'),
    path('valida_servico', views.valida_servico, name='valida_servico'),
    path('edita_produto/<int:id>', views.edita_produto, name='edita_produto'),
    path('edita_servico/<int:id>', views.edita_servico, name='edita_servico'),
    path('excluir_produto/<int:id>', views.excluir_produto, name='excluir_produto'),
    path('excluir_servico/<int:id>', views.excluir_servico, name='excluir_servico'),
]