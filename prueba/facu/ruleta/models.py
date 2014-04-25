from django.db import models
from jsonfield import JSONField
import collections
import random


# Create your models here.
class Tirada(models.Model):
    descripcion = models.CharField(max_length=64)
    numeros = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})

    @classmethod
    def create(self, descripcionTirada):
        tirada = Tirada(descripcion=descripcionTirada)
        aleatorios = []
        acumMedia = 0.00
        resultMedia = 0.00
        for i in xrange(0, 10001):
            lista = [i, random.randint(0, 36)]
            acumMedia += lista[1]
            resultMedia = acumMedia / (i + 1)
            lista.append(resultMedia)
            aleatorios.append(lista)
        tirada.numeros = aleatorios
        tirada.save()
        return tirada



