from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from catalogo.defines import CATEGORIA_BICI_CHOICES
from catalogo.defines import CATEGORIA_EQUIPAMIENTO_CHOICES
from catalogo.defines import CATEGORIA_CATALOGO_CHOICES
from catalogo.defines import ESTADO_BICI_CHOICES
from catalogo.defines import ESTADO_EQUIPAMIENTO_CHOICES


# Create your models here.

class Sede(models.Model):
    nombre_sede = models.CharField(max_length = 20)
    ciudad_sede = models.CharField(max_length = 20)

    def __str__(self):
        return "nombre:'%s', ciudad:'%s'" % (self.nombre_sede, self.ciudad_sede)

class Catalogo(models.Model):
    codigo = models.PositiveIntegerField(null=True, blank=True)
    tipo_catalogo = models.CharField(max_length = 50, choices = CATEGORIA_CATALOGO_CHOICES)

    def __str__(self):
        return "Codigo:'%s', Tipo_Catalogo:'%s' " % (self.codigo, self.tipo_catalogo)

class Equipamiento(models.Model):
    id_equipamiento = models.PositiveIntegerField(null=False, primary_key=True, default="DEFECTO")
    tipo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, null=True)
    tipo_equipamiento = models.CharField(max_length= 100, default=None, choices = CATEGORIA_EQUIPAMIENTO_CHOICES)
    precio_equipamiento = models.PositiveIntegerField(null=True, blank=True)
    descripcion_equipamiento = models.CharField(max_length = 200, null=True, blank=True)
    estado_equipamiento = models.CharField(max_length = 20, null=True, blank=True, choices = ESTADO_EQUIPAMIENTO_CHOICES)
    ubicacion_equipamiento = models.CharField(max_length = 100, default=None)
    imagen_equipamiento = models.ImageField(upload_to = 'imagenes_equipamiento', null=True, blank=True)

    def __str__(self):
        return "id_equip:'%s', tipo:'%s', precio:'%s', estado:'%s', ubicacion:'%s' " % (self.id_equipamiento, self.tipo_equipamiento, self.precio_equipamiento, self.estado_equipamiento, self.ubicacion_equipamiento)

class Bicicleta(models.Model):
    id_bicicleta = models.CharField(max_length=45, null=False, primary_key=True, default="DEFECTO")
    tipo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, null=True)
    marca = models.CharField(max_length=20)
    aro = models.PositiveIntegerField(blank=True)
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    estado_bicicleta = models.CharField(max_length = 20, null=True, blank=True, choices = ESTADO_BICI_CHOICES)
    descripcion_bicicleta = models.CharField(max_length = 200, null=True, blank=True)
    ubicacion_bicicleta = models.CharField(max_length = 100, default=None)
    precio_bicicleta = models.PositiveIntegerField(null=True, blank=True)
    tipo_bicicleta = models.CharField(max_length = 20, null=True, blank=True, choices = CATEGORIA_BICI_CHOICES)
    imagen_bicicleta = models.ImageField(upload_to = 'imagenes_bicicletas', null=True, blank=True)

    def __str__(self):
        return "id_bicicleta: '%s', tipo_catalogo: '%s', marca:'%s', aro: '%s', cantidad: '%s', estado: '%s', ubicacion:'%s', precio:'%s', tipo_bicicleta:'%s'" % (self.id_bicicleta, self.tipo, self.marca, self.aro, self.cantidad, self.estado_bicicleta, self.ubicacion_bicicleta, self.precio_bicicleta, self.tipo_bicicleta)