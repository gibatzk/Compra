from django.db import models

class Propriedades(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    telefone = models.IntegerField()
    cultivar = models.CharField(max_length=50)  #alface
    hectare = models.CharField(max_length=50)
    produção_mês_quantidade = models.IntegerField()


