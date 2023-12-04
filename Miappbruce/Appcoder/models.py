from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.TextField()

class Cliente(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    email = models.EmailField()

class RecursoHumano(models.Model):
    Nombre = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)