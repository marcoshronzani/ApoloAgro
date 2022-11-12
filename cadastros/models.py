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
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    observacao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Produto'


    def __str__(self):
        return self.descricao


class Clientes(models.Model):
    nome_completo = models.CharField(max_length=100, blank=True)
    nome_fantasia = models.CharField(max_length=100, blank=True)
    razao_social = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    rg = models.CharField(max_length=9, blank=True)
    inscricao_est = models.CharField(max_length=9, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    telefone_2 = models.CharField(max_length=15, blank=True)
    contato = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=60, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    fisica = models.BooleanField




