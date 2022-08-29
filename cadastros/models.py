from django.db import models


class Categorias(models.Model):
    descricao = models.CharField(max_length = 50)
    produto = models.BooleanField(default = False)
    servico = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.descricao


class Servicos(models.Model):
    descricao = models.CharField(max_length= 50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Servico'

    def __str__(self):
        return self.descricao


class Produtos(models.Model):
    descricao = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    observacao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Produto'


    def __str__(self):
        return self.descricao