from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')  

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class Orden(models.Model):
    
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    productos = models.ManyToManyField(Producto, through='OrdenProducto')  
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente') 
    fecha = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Orden de {self.usuario.username} - {self.total}$ - {self.estado}"

class OrdenProducto(models.Model):
   
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()  
    

