from django.db import models

class Compradores(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    telefone = models.IntegerField()
    cultivar = models.CharField(max_length=50)
    hectare = models.CharField(max_length=50)