from django.contrib import admin
from .models import Categorias, Produtos, Servicos, Clientes

admin.site.register(Categorias)
admin.site.register(Produtos)
admin.site.register(Servicos)
admin.site.register(Clientes)
