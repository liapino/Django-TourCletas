from django.shortcuts import render, redirect
from .models import Bicicleta
from django.shortcuts import get_object_or_404

# Create your views here.

def catalogo(request):
    template_name = "catalogo/catalogo.html"
    #print (Bicicleta.objects.all)
    #bicicleta = get_object_or_404(Bicicleta, marca = 'bianchi')
    for x in Bicicleta.objects.all():
        print (x.aro)

    #print (bicicleta.aro)
    return render(request, template_name, {'catalogo':catalogo})
