# Generated by Django 4.1 on 2022-11-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_clientes_bairro_clientes_celular_clientes_cep_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='telefone_2',
        ),
        migrations.AddField(
            model_name='clientes',
            name='tipo',
            field=models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], max_length=1, null=True),
        ),
    ]
