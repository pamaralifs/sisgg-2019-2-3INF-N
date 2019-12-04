# Generated by Django 3.0 on 2019-12-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=140, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=40, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=8, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino'], ['N', 'Nenhuma das opções']], max_length=1, verbose_name='Sexo'),
        ),
    ]
