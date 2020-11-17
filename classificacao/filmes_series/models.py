from django.db import models

class Filme(models.Model):
    duracao = models.CharField(max_length=10)
    titulo = models.CharField(max_length=15)
    descricao = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField(max_length=30)
    star = models.IntegerField()


class Serie(models.Model):
    temporada = models.IntegerField()
    titulo = models.CharField(max_length=15)
    descricao = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField(max_length=30)
    star = models.IntegerField()

# Create your models here.
