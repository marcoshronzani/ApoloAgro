# Generated by Django 4.1 on 2023-08-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0029_alter_clientes_cnpj_alter_clientes_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
