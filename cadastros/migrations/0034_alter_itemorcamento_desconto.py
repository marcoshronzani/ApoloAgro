# Generated by Django 4.1 on 2023-11-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0033_rename_valor_orcamentos_valor_desconto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorcamento',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
