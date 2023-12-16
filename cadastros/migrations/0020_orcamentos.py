# Generated by Django 4.1 on 2023-04-17 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0019_alter_clientes_cnpj_alter_clientes_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(default=datetime.date.today)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Orcamento',
            },
        ),
    ]