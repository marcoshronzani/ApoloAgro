# Generated by Django 4.1 on 2022-11-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_clientes_remove_produtos_fabricante'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='bairro',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='clientes',
            name='celular',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cep',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='clientes',
            name='complemento',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contato',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='clientes',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='clientes',
            name='inscricao_est',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AddField(
            model_name='clientes',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='clientes',
            name='numero',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='clientes',
            name='razao_social',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='clientes',
            name='rg',
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AddField(
            model_name='clientes',
            name='site',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='clientes',
            name='telefone_2',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
