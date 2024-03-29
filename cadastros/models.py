from datetime import date
from django.db import models
from .choices import EstadosBr
from usuarios.models import Usuario


class Categorias(models.Model):
    descricao = models.CharField(max_length=50)
    produto = models.BooleanField(default=False)
    servico = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Categoria"

    def __str__(self):
        return self.descricao


class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=30)
    sigla = models.CharField(max_length=4)

    class Meta:
        verbose_name = "UnidadeMedida"

    def __str__(self):
        return self.descricao


class Servicos(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)
    und = models.ForeignKey(UnidadeMedida, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Servico"

    def __str__(self):
        return self.descricao


class Produtos(models.Model):
    descricao = models.CharField(max_length=50)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    observacao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)
    und = models.ForeignKey(UnidadeMedida, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Produto"

    def __str__(self):
        return self.descricao


class Clientes(models.Model):
    choices = (("F", "Física"), ("J", "Jurídica"))
    nome_completo = models.CharField(max_length=100, blank=True)
    nome_fantasia = models.CharField(max_length=100, blank=True)
    razao_social = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=18, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    rg = models.CharField(max_length=9, blank=True)
    inscricao_est = models.CharField(max_length=9, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    contato = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    site = models.URLField(max_length=100, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(
        max_length=2, blank=True, null=True, choices=EstadosBr.choices
    )
    tipo = models.CharField(max_length=1, choices=choices, null=True)
    cord_geografica = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"

    def __str__(self):
        return self.razao_social


class Terceiros(models.Model):
    choices = (("F", "Física"), ("J", "Jurídica"))
    nome_completo = models.CharField(max_length=100, blank=True)
    nome_fantasia = models.CharField(max_length=100, blank=True)
    razao_social = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=18, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    rg = models.CharField(max_length=9, blank=True)
    inscricao_est = models.CharField(max_length=9, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    contato = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    site = models.URLField(max_length=100, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    logradouro = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(
        max_length=2, blank=True, null=True, choices=EstadosBr.choices
    )
    tipo = models.CharField(max_length=1, choices=choices, null=True)
    cord_geografica = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Terceiro"

    def __str__(self):
        return self.razao_social


class Orcamentos(models.Model):
    choice = (
        ('AB', 'Aberto'),
        ('AN', 'Em Andamento'),
        ('PA', 'Pausado'),
        ('AR', 'Aguardando Retorno'),
        ('FN', 'Finalizado')
    )
    data_criacao = models.DateField(default=date.today)
    situacao = models.CharField(max_length=2, choices=choice)
    observacao = models.TextField(null=True, blank=True)
    desconto = models.FloatField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    terceiro = models.ForeignKey(Terceiros, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Orcamento"

    def __str__(self):
        return f"Orçamento: {self.id}"

    @property
    def valor_total_orcamento(self):
        total = 0
        for item in self.itens.all():
            total += item.item_valor
        return total


class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(
        Orcamentos, on_delete=models.CASCADE, related_name="itens"
    )
    item_produto = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    item_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade = models.IntegerField()
    desconto = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = "itemOrcamento"

    def __str__(self):
        return f"Orçamento: {self.orcamento.id} | Valor: {self.item_valor}"



class ItemOrcamentoServico(models.Model):
    orcamento = models.ForeignKey(
        Orcamentos, on_delete=models.CASCADE, related_name="itens_servicos"
    )
    item_servico = models.ForeignKey(Servicos, on_delete=models.DO_NOTHING)
    item_valor_servico = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    desconto = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "itemOrcamentoServico"

    def __str__(self):
        return f"Orçamento: {self.orcamento.id} | Valor: {self.item_valor}"
