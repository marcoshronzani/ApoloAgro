# Generated by Django 4.1 on 2023-04-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('cadastros', '0020_orcamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamentos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
