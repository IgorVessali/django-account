# Generated by Django 3.2 on 2021-04-07 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='Número')),
                ('initial_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo Inicial')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('operation', models.CharField(choices=[('C', 'Credito'), ('D', 'Debito')], max_length=1, verbose_name='Operação')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='account.account')),
            ],
            options={
                'verbose_name': 'history',
                'verbose_name_plural': 'histories',
            },
        ),
    ]
