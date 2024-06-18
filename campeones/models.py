from django.db import models

# Create your models here.

class Campeon(models.Model):
    nombre = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    edad = models.IntegerField()
    es_mago = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.region} - {self.nombre}'


class User(models.Model):
    nombre = models.CharField(max_length=128)
    campeones = models.ManyToManyField(Campeon, blank=True)

    def __str__(self):
        return self.nombre