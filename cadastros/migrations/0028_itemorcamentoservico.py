# Generated by Django 4.1 on 2023-05-25 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0027_alter_itemorcamento_orcamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrcamentoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_valor_servico', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
                ('item_servico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.servicos')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_servicos', to='cadastros.orcamentos')),
            ],
            options={
                'verbose_name': 'itemOrcamentoServico',
            },
        ),
    ]
