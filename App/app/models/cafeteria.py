from django.db import models

class Cafeteria(models.Model):

    nome_cafeteria = models.CharField(max_length=250)
    local = models.CharField(max_length=250)