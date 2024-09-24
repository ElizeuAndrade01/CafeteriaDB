from django.db import models

class Cafeteria(models.Model):

    nome_cafeteria = models.CharField(max_length=250)
    local = models.CharField(max_length=250)

class Cliente(models.Model):

    nome_cliente = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=250)

class Empregado(models.Model):

    nome_empregado = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=250)
    salario = models.PositiveBigIntegerField()
    id_cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)

class Produto(models.Model):

    nome_produto = models.CharField(max_length=250)
    preco = models.FloatField()

class Compra(models.Model):

    datahora_compra = models.DateTimeField(max_length=250)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empregado = models.ForeignKey(Empregado, on_delete=models.CASCADE)
    id_cafeteria_empregado = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Compra_Produto(models.Model):

    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Produto_Cafeteria(models.Model):

    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    quantidade = models.IntegerField()