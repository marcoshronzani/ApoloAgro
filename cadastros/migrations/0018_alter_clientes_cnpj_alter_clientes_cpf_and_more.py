# Generated by Django 4.1 on 2023-01-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0017_alter_clientes_estado_alter_terceiros_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='terceiros',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
