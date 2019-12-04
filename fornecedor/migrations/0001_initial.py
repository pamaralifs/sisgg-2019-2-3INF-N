# Generated by Django 3.0 on 2019-12-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome/Razão Social')),
                ('cnpj', models.CharField(help_text='(Formato 99.999.999/9999-99)', max_length=19, unique=True, verbose_name='CNPJ')),
                ('ddd_telefone', models.CharField(help_text='(Formato 99)', max_length=2, verbose_name='DDD')),
                ('telefone', models.CharField(help_text='(Formato 99999-9999)', max_length=10, verbose_name='Telefone')),
            ],
        ),
    ]
