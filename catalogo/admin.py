from django.contrib import admin
from catalogo.models import Bicicleta, Equipamiento, Sede

@admin.register(Bicicleta)
class bicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca','aro', 'cantidad','estado_bicicleta', 'descripcion_bicicleta', 'ubicacion_bicicleta','precio_bicicleta','tipo_bicicleta','imagen_bicicleta',)

@admin.register(Equipamiento)
class equipamientoAdmin(admin.ModelAdmin):
	list_display = ('tipo_equipamiento','precio_equipamiento','descripcion_equipamiento','estado_equipamiento','ubicacion_equipamiento','imagen_equipamiento',)

@admin.register(Sede)
class sedeAdmin(admin.ModelAdmin):
	list_display = ('nombre_sede','ciudad_sede',)


