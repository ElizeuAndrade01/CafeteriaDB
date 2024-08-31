from django.db import models
import cafeteria

class Empregado(models.Model):

    nome_empregado = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=250)
    salario = models.PositiveBigIntegerField()
    id_cafeteria = models.ForeignKey(cafeteria.Cafeteria, on_delete=models.CASCADE)