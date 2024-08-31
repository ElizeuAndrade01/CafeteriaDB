from django.db import models
import cliente
import empregado
import produto

class Compra(models.Model):
    datahora_compra = models.DateTimeField(max_length=250)
    id_cliente = models.ForeignKey(cliente.Cliente, on_delete=models.CASCADE)
    id_empregado = models.ForeignKey(empregado.Empregado, on_delete=models.CASCADE)
    id_cafeteria_empregado = models.ForeignKey(empregado.Empregado.id_cafeteria, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(produto.Produto, on_delete=models.CASCADE)