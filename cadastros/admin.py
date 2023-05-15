from django.contrib import admin
from .models import Categorias, Produtos, Servicos, Clientes, Terceiros, UnidadeMedida, Orcamentos, ItemOrcamento

admin.site.register(Categorias)
admin.site.register(Produtos)
admin.site.register(Servicos)
admin.site.register(Clientes)
admin.site.register(Terceiros)
admin.site.register(UnidadeMedida)
admin.site.register(Orcamentos)
admin.site.register(ItemOrcamento)
