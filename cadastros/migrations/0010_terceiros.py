# Generated by Django 4.1 on 2022-12-01 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_alter_clientes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terceiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(blank=True, max_length=100)),
                ('nome_fantasia', models.CharField(blank=True, max_length=100)),
                ('razao_social', models.CharField(blank=True, max_length=100)),
                ('cnpj', models.CharField(blank=True, max_length=14)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('rg', models.CharField(blank=True, max_length=9)),
                ('inscricao_est', models.CharField(blank=True, max_length=9)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('contato', models.CharField(blank=True, max_length=30)),
                ('celular', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('site', models.URLField(blank=True, max_length=100)),
                ('cep', models.CharField(blank=True, max_length=10)),
                ('logradouro', models.CharField(blank=True, max_length=100)),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('bairro', models.CharField(blank=True, max_length=30)),
                ('cidade', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('tipo', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Terceiro',
            },
        ),
    ]