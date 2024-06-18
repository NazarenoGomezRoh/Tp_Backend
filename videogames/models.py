from django.db import models

# Create your models here.

class Videogames(models.Model):
    nombre = models.CharField(max_length=128)
    anio = models.IntegerField()
    genero = models.CharField(max_length=128)
    es_goty = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} - {self.anio}'


class User(models.Model):
    nombre = models.CharField(max_length=128)
    videogames = models.ManyToManyField(Videogames, blank=True)

    def __str__(self):
        return self.nombre