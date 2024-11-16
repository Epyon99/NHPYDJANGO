from django.db import models

# Create your models here.
class Proveedor(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/',null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    proveedor = models.ForeignKey(Proveedor,related_name='productos', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

