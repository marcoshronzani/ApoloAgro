from django.db import models


class Categorias(models.Model):
    descricao = models.CharField(max_length = 50)
    tipo = models.BooleanField()

    class Meta:
        verbose_name = 'Categoria'