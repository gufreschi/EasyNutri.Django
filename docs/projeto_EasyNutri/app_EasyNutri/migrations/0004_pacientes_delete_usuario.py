# Generated by Django 4.2.6 on 2023-11-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_EasyNutri', '0003_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
