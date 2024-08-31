from django.db import models
import produto
import cafeteria

class Produto_Cafeteria(models.Model):
    id_produto = models.ForeignKey(produto.Produto, on_delete=models.CASCADE)
    id_cafeteria = models.ForeignKey(cafeteria.Cafeteria, on_delete=models.CASCADE)
    quantidade = models.IntegerField()