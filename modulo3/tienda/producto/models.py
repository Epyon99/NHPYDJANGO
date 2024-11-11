from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productos/',null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,blank=False)
    
    def __str__(self):
        return self.name
