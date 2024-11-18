from django.shortcuts import render
from django.shortcuts import render , HttpResponse 
from Servicios.models import Servicio

# Create your views here.




def home (request):
    return render(request,"TiendaHApp/Home.html")

def tienda (request):
    return render(request,"TiendaHApp/Tienda.html")


def AvisoLegal(request):
    return render(request,"TiendaHApp/AvisoLegal.html")

