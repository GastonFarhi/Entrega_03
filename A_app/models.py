from django.db import models


# Create your models here.
class Disco(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


class Remera(models.Model):
    disenio = models.CharField(max_length=100)
    talle = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.disenio} - {self.talle}"


class Libros(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.autor} - {self.titulo}"
