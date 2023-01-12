from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Categorias, Clientes, Terceiros, UnidadeMedida


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = (
            'descricao',
            'produto',
            'servico'
        )
        labels = {
            'descricao': 'Descrição'
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if Categorias.objects.filter(descricao=descricao).exists():
            raise ValidationError('Já existe essa descrição, faça outra!')

        return descricao


class UndMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadeMedida
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if Clientes.objects.filter(cnpj=cnpj).exists():
            raise ValidationError('CNPJ já Cadastrado.')

        return cnpj

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Clientes.objects.filter(cpf=cpf).exists():
            raise ValidationError('CPF já Cadastrado.')
        
        return cpf


class TerceiroForm(forms.ModelForm):
    class Meta:
        model = Terceiros
        fields = (
            'nome_completo',
            'nome_fantasia',
            'razao_social',
            'cnpj',
            'cpf',
            'rg',
            'inscricao_est',
            'telefone',
            'contato',
            'celular',
            'email',
            'site',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'tipo'
        )
    
        def clean_cnpj(self):
            cnpj = self.cleaned_data.get('cnpj')
            if Clientes.objects.filter(cnpj=cnpj).exists():
                raise ValidationError('CNPJ já Cadastrado.')

            return cnpj

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Clientes.objects.filter(cpf=cpf).exists():
            raise ValidationError('CPF já Cadastrado.')
        
        return cpf