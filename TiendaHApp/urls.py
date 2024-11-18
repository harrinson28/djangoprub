from django.urls import path
from TiendaHApp import views


urlpatterns = [
    path("home",views.home, name="home"),
    
    path("tienda",views.tienda, name="tienda"),
    
    path("AvisoLegal",views.AvisoLegal,name="AvisoLegal"),
]