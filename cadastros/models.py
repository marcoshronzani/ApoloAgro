from django.db import models


class Categorias(models.Model):
    descricao = models.CharField(max_length = 50)
    produto = models.BooleanField(default = False)
    servico = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.descricao