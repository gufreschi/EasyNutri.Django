# Generated by Django 4.2.6 on 2023-10-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_EasyNutri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]
