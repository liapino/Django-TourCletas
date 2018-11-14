from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def catalogo(request):
    template_name = "catalogo/catalogo.html"
    #catalogo = Catalogo.objects.all()
    
    for i in Catalogo.objects.all():
        print("---------")
        print (i.bicicleta.marca)
    
    return render(request, template_name, {'catalogo':Catalogo.objects.all()})