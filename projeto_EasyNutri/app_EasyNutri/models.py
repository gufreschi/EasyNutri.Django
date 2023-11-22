from django.db import models

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()