from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import *

# Create your views here.
def catalogo(request):
	data = {}
	data['bicicleta'] = Bicicleta.objects.all()
	data['equipamiento'] = Equipamiento.objects.all()
	template_name = 'catalogo.html'
	return render(request, template_name, data)

def ver_mas_bicicletas(request, id_detalles):
	data = {}
	data['bicicleta'] = Bicicleta.objects.get(pk=id_detalles)
	
	template_name = 'ver_mas_bicicletas.html'
	return render(request, template_name, data)

def ver_mas_equipamiento(request, id_detalles):
	data = {}
	data['bicicleta'] = Bicicleta.objects.get(pk=id_detalles)
	data['equipamiento'] = Equipamiento.objects.get(pk=id_detalles)
	template_name = 'ver_mas_equipamiento.html'
	return render(request, template_name, data)

"""	
def detalles(request, id_detalles):
	lista = []
	data = {}
	data['bicicleta'] = Bicicleta.objects.get(pk=id_detalles)
	template_name = 'buscar.html'
	return render(request, template_name, data)
	#{'clave':'key'}
"""

