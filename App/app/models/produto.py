from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=250)
    preco = models.FloatField()