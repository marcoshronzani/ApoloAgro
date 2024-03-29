# Generated by Django 4.1 on 2023-07-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0028_itemorcamentoservico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cpf',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
