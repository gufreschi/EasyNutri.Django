# Generated by Django 4.2.6 on 2023-11-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_EasyNutri', '0006_paciente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
    ]