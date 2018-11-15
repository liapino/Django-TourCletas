from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import *

# Create your views here.
def catalogo(request):
	data = {}
	data['bicicleta'] = Bicicleta.objects.all()
	template_name = 'catalogo.html'
	return render(request, template_name, data)

def ver_mas(request):
	template_name = 'ver_mas.html'
	return render(request, template_name)
	

