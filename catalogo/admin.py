from django.contrib import admin
from catalogo.models import Bicicleta, Equipamiento, Sede

@admin.register(Bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca','aro', 'cantidad','estado', 'ubicacion','precio','tipo_bicicleta','imagen',)

@admin.register(Equipamiento)
class equipamientoAdmin(admin.ModelAdmin):
	list_display = ('tipo_equipamiento','precio_equipamiento',)

@admin.register(Sede)
class sedeAdmin(admin.ModelAdmin):
	list_display = ('nombre_sede','ciudad_sede',)


