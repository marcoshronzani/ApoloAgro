from django.contrib import admin
from .models import Categorias, Produtos, Servicos

admin.site.register(Categorias)
admin.site.register(Produtos)
admin.site.register(Servicos)

