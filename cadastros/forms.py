from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Categorias, Clientes


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


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        