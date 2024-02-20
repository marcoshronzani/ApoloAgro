from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.clientes, name="clientes"),
    path("categorias/", views.categorias, name="categorias"),
    path("cria_categoria/", views.criar_categoria, name="cria_categoria"),
    path("edita_categoria/<int:id>", views.edita_categoria, name="edita_categoria"),
    path(
        "exluir_categoria/<int:id>", views.excluir_categoria, name="excluir_categoria"
    ),
    path("produtos/", views.produtos, name="produtos"),
    path("cria_produto/", views.cria_produto, name="cria_produto"),
    path("cria_servico/", views.cria_servico, name="cria_servico"),
    path("servicos/", views.servicos, name="servicos"),
    path("valida_produto", views.valida_produto, name="valida_produto"),
    path("valida_servico", views.valida_servico, name="valida_servico"),
    path("edita_produto/<int:id>", views.edita_produto, name="edita_produto"),
    path("edita_servico/<int:id>", views.edita_servico, name="edita_servico"),
    path("excluir_produto/<int:id>", views.excluir_produto, name="excluir_produto"),
    path("excluir_servico/<int:id>", views.excluir_servico, name="excluir_servico"),
    path("busca_cat/", views.busca_cat, name="busca_cat"),
    path("clientes/", views.clientes, name="clientes"),
    path("cria_cliente/", views.cria_cliente, name="cria_cliente"),
    path("exclui_cliente/<int:id>", views.excluir_cliente, name="excluir_cliente"),
    path("edita_cliente/<int:id>", views.edita_cliente, name="edita_cliente"),
    path("terceiros/", views.terceiros, name="terceiros"),
    path("cria_terceiro/", views.cria_terceiro, name="cria_terceiro"),
    path("edita_terceiro/<int:id>", views.edita_terceiro, name="edita_terceiro"),
    path("exclui_terceiro/<int:id>", views.excluir_terceiro, name="excluir_terceiro"),
    path("unidade_medida/", views.unidade_medida, name="und_medidas"),
    path("cria_und_medida/", views.cria_und_medida, name="cria_und"),
    path("excluir_und_medida/<int:id>", views.excluir_und_medida, name="excluir_und"),
    path("edita_und_medida/<int:id>", views.edita_und_medida, name="edita_und_medida"),
    path("orcamentos/", views.orcamentos, name="orcamentos"),
    path("cria_orcamento/", views.cria_orcamento, name="cria_orcamento"),
    path("edita_orcamento/<int:id>", views.edita_orcamento, name="edita_orcamento"),
    path("excluir_orcamento/<int:id>", views.excluir_orcamento, name="excluir_orcamento"),
    path("item_orcamento/<int:id>", views.item_orcamento, name="item_orcamento"),
    path(
        'adicionar_item_orcamento/<int:id_orcamento>',
        views.adicionar_item_orcamento,
        name='adicionar_item_orcamento'
    ),
    path("excluir_item/<int:id>", views.excluir_item_orcamento, name="excluir_item"),
]
