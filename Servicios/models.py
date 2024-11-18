from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    #Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    class meta:
        verbose_name="servicio"
        verbose_name_plural = "servicios"
        
    def __str__(self):
        return self.titulo