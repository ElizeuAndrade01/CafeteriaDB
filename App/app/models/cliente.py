from django.db import models

class Cliente(models.Model):

    nome_cliente = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=250)