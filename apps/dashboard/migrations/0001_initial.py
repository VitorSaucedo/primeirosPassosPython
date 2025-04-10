# Generated by Django 5.2 on 2025-04-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('vendas', models.PositiveIntegerField(default=0)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-vendas'],
            },
        ),
    ]
