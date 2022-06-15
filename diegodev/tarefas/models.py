from django.db import models


# Modelo da tabela de banco de dados. Para criar as tabelas, basta ´da o comando python manage.py makemigrations
class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)
