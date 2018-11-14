from django.shortcuts import render, redirect
from .models import Bicicleta
from django.shortcuts import get_object_or_404
from .models import Catalogo


# Create your views here.

def catalogo(request):
    template_name = "catalogo/catalogo.html"
    #catalogo = Catalogo.objects.all()
    
    for i in Catalogo.objects.all():
        print("---------")
        print (i.bicicleta.marca)
    
    return render(request, template_name, {'catalogo':Catalogo.objects.all()})

"""
def editar_post(request):
    template_name = "index.html"
    if request.POST:
        formulario = edit_post(request.POST, request.FILES)
    return render(request, template_name, {})
"""