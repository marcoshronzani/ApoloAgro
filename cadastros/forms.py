from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Categorias, Clientes, Terceiros, UnidadeMedida, Orcamentos, ItemOrcamento


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
        labels = {
            'nome_completo': 'Nome Completo',
            'nome_fantasia': 'Nome Fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'cpf': 'CPF',
            'rg': 'RG',
            'inscricao_est': 'Inscrição Estadual',
            'cep': 'CEP',
            'numero': 'Número',
            'cord_geografica': 'Coordenada Geográfica'
        }
            
    def clean(self):

        super(ClienteForm, self).clean()

        if 'tipo' in self.cleaned_data:
            tipo_cliente = self.cleaned_data['tipo']
            cnpj = self.cleaned_data.get('cnpj')
            cpf = self.cleaned_data.get('cpf')
            
            if tipo_cliente == 'J' and cnpj == '':
                self.add_error(
                    'cnpj', 'CNPJ Obrigatório'
                )
                raise ValidationError('CNPJ Obrigatório')
                
            if tipo_cliente =='J' and not (cnpj.isdigit()):
                self.add_error(
                'cnpj', 'Somente Números'
                )
                raise ValidationError('Somente Números')

            if cnpj != '':
                if Clientes.objects.filter(cnpj=cnpj).exists():
                    self.add_error(
                        'cnpj', 'CNPJ já Cadastrado'
                    )
                    raise ValidationError('CNPJ já Cadastrado.')

            if tipo_cliente == 'F' and cpf == '':
                self.add_error(
                    'cpf', 'CPF Obrigatório'
                )
                raise ValidationError('CPF Obrigatório')
                
            if tipo_cliente =='F' and not (cpf.isdigit()):
                self.add_error(
                'cpf', 'Somente Números'
                )
                raise ValidationError('Somente Números')
            print(cpf)
            if cpf != '':
                if Clientes.objects.filter(cpf=cpf).exists():
                    self.add_error(
                        'cpf', 'CPF já Cadastrado'
                    )
                    raise ValidationError('CPF já Cadastrado.')
            
        
        return self.cleaned_data


class ClienteEdtForm(ClienteForm):
    def clean(self):
        pass


class TerceiroForm(forms.ModelForm):
    class Meta:
        model = Terceiros
        fields = '__all__'
        labels = {
            'nome_completo': 'Nome Completo',
            'nome_fantasia': 'Nome Fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'cpf': 'CPF',
            'rg': 'RG',
            'inscricao_est': 'Inscrição Estadual',
            'cep': 'CEP',
            'numero': 'Número',
            'cord_geografica': 'Coordenada Geográfica'
        }
    
    def clean(self):

        super(TerceiroForm, self).clean()

        if 'tipo' in self.cleaned_data:
            tipo_terceiro = self.cleaned_data['tipo']
            cnpj = self.cleaned_data.get('cnpj')
            cpf = self.cleaned_data.get('cpf')
            
            if tipo_terceiro == 'J' and cnpj == '':
                self.add_error(
                    'cnpj', 'CNPJ Obrigatório'
                )
                raise ValidationError('CNPJ Obrigatório')
                
            if not (cnpj.isdigit()) and tipo_terceiro =='J':
                self.add_error(
                'cnpj', 'Somente Números'
                )
                raise ValidationError('Somente Números')
            
            if cnpj != '':
                if Clientes.objects.filter(cnpj__exact=cnpj).exists():
                    self.add_error(
                        'cnpj', 'CNPJ já Cadastrado'
                    )
                    raise ValidationError('CNPJ já Cadastrado.')

            if tipo_terceiro == 'F' and cpf == '':
                self.add_error(
                    'cpf', 'CPF Obrigatório'
                )
                raise ValidationError('CPF Obrigatório')
                
            if not (cpf.isdigit()) and tipo_terceiro =='F':
                self.add_error(
                'cpf', 'Somente Números'
                )
                raise ValidationError('Somente Números')
            
            if cpf != '':
                if Clientes.objects.filter(cpf=cpf).exists():
                    self.add_error(
                        'cpf', 'CPF já Cadastrado'
                    )
                    raise ValidationError('CPF já Cadastrado.')
            
        
        return self.cleaned_data
    

class TerceiroEdtForm(TerceiroForm):
    def clean(self):
        pass


class OrcamentoForm(forms.ModelForm):

    class Meta:
        model = Orcamentos
        fields = '__all__'
        widgets = {
            'data_criacao': forms.DateInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }


class ItemOrcaForm(forms.ModelForm):
    
    class Meta:
        model = ItemOrcamento
        fields = '__all__'
        widgets = {
            'item_produto': forms.Select(attrs={'class': 'form-control col-md-3 '}),
            'item_valor': forms.NumberInput(attrs={'class': 'form-control col-md-2'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control col-md-2'})
        }

