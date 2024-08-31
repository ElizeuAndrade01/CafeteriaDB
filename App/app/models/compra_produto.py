from django.db import models
import produto
import compra

class Produto_Cafeteria(models.Model):
    id_produto = models.ForeignKey(produto.Produto, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(compra.Compra, on_delete=models.CASCADE)
    quantidade = models.IntegerField()