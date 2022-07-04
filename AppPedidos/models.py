from pyexpat import model
from random import choices
from django.db import models

# Create your models here.
class Clientes(models.Model):
    Cuit=models.CharField(max_length=10)
    RSocial=models.CharField(max_length=40)
    Domicilio=models.CharField(max_length=40)
    Mail=models.EmailField()
    Telefono=models.CharField(max_length=10)
    Activo=models.BooleanField()
    
    def __str__(self):
        return self.RSocial
    
class Marca (models.Model):
    nombre=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Articulos(models.Model):
    Codigo=models.CharField(max_length=10)
    Descripcion=models.CharField(max_length=40)
    UnidadMedida=models.CharField(max_length=3)
    Precio=models.IntegerField()
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    Imagen=models.ImageField(upload_to="productos",null=True)
    
    def __str__(self):
        return self.Descripcion
    
class Pedidos(models.Model):
    NroPedido=models.IntegerField()
    Fecha=models.DateField()
    CuitCliente=models.CharField(max_length=10)
    Importe=models.IntegerField()
    
    def __str__(self):
        return self.NroPedido
    
    
    
class PedidoDetalle(models.Model):
    NroPedido=models.IntegerField()
    Articulo=models.CharField(max_length=10)
    Cantidad=models.IntegerField()
    Punitario=models.IntegerField()
    
    def __str__(self):
        return self.NroPedido
    
    
opciones_consultas=[
        [0,"consulta"],
        [1,"reclamo"],
        [2,"sugerencia"],
        [3,"otros"]
    ]
class Contacto(models.Model):
        nombre=models.CharField(max_length=50)
        correo = models.EmailField()
        tipo_consulta = models.IntegerField(choices=opciones_consultas)
        mensaje=models.TextField()
        avisos=models.BooleanField()
        
        def __str__(self):
            return self.nombre