from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from catalogo.defines import CATEGORIA_BICI_CHOICES
from catalogo.defines import CATEGORIA_EQUIPAMIENTO_CHOICES
from catalogo.defines import CATEGORIA_CATALOGO_CHOICES


# Create your models here.


class Bicicleta(models.Model):
    marca = models.CharField(max_length=20)
    aro = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    estado = models.PositiveIntegerField(null=True, blank=True)
    ubicacion = models.CharField(max_length = 100, default=None)
    precio = models.PositiveIntegerField(null=True, blank=True)
    tipo_bicicleta = models.CharField(max_length = 20, default=None, choices = CATEGORIA_BICI_CHOICES)
    imagen = models.ImageField(upload_to = 'imagenes_bicicletas', null=True, blank=True)

    def __str__(self):
        return "marca:'%s', aro: '%s', cantidad: '%s', estado: '%s', ubicacion:'%s', precio:'%s', tipo_bicicleta:'%s'" % (self.marca, self.aro, self.cantidad, self.estado, self.ubicacion, self.precio, self.tipo_bicicleta)

class Equipamiento(models.Model):
    tipo_equipamiento = models.CharField(max_length= 100, default=None, choices = CATEGORIA_EQUIPAMIENTO_CHOICES)
    precio_equipamiento = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "tipo:'%s', precio:'%s' " % (self.tipo_equipamiento, self.precio_equipamiento)

class Sede(models.Model):
    nombre_sede = models.CharField(max_length = 20)
    ciudad_sede = models.CharField(max_length = 20)

    def __str__(self):
        return "nombre:'%s', ciudad:'%s'" % (self.nombre_sede, self.ciudad_sede)

class Catalogo(models.Model):
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE, null=True)
    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE, null=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
    tipo_catalogo = models.CharField(max_length = 50, choices = CATEGORIA_CATALOGO_CHOICES)
    codigo = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "Bicicleta:'%s', Equipamiento:'%s', Sede:'%s', Tipo_catalogo:'%s', codigo:'%s'" % (self.bicicleta, self.equipamiento, self.sede, self.tipo_catalogo, self.codigo)









