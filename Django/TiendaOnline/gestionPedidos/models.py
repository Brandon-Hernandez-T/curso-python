from django.db import models

# Una clase por cada Tabla
#Tabla: Clientes
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

#Tabla: Articulos
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

#Tabla: Pedidos
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.IntegerField()
    entregado=models.BooleanField()
