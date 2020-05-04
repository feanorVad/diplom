from django.db import models


class Abonent(models.Model):
    contract = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    adres = models.CharField(max_length=200)
    bank = models.TextField(max_length=500)
    unp = models.CharField(max_length=7)
    kontact = models.CharField(max_length=50)
    preabon = models.CharField(max_length=50)
    pasport = models.CharField(max_length=20)


class Tarif (models.Model):
    method = models.CharField(max_length=20)
    tarif = models.CharField(max_length=20)
    schet = models.CharField(max_length=50)
    money = models.CharField(max_length=3)
    contract = models.ForeignKey(
        Abonent,
        on_delete=models.CASCADE,
    )