# Generated by Django 4.1 on 2022-11-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_remove_clientes_telefone_2_clientes_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='site',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]