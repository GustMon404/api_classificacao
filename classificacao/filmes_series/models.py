from django.db import models

class Filme(models.Model):
    tipo = models.CharField(max_length=10)
    titulo = models.CharField(max_length=15)
    descricao = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField(max_length=30)
    star = models.IntegerField()
    duracao = models.CharField(max_length=10)

class Serie(models.Model):
    tipo = models.CharField(max_length=10)
    titulo = models.CharField(max_length=15)
    descricao = models.TextField()
    ano = models.IntegerField()
    genero = models.CharField(max_length=30)
    star = models.IntegerField()
    temporada = models.IntegerField()
# Create your models here.
