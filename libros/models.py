from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=128)
    autor = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    es_tapa_dura = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.autor} - {self.nombre}'


class User(models.Model):
    nombre = models.CharField(max_length=128)
    libros = models.ManyToManyField(Libros, blank=True)

    def __str__(self):
        return self.nombre