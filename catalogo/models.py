from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bicicleta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marca = models.CharField(max_length=20)
    aro = models.IntegerField()

class Equipamiento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caso = models.IntegerField()
    rodillera = models.IntegerField()







