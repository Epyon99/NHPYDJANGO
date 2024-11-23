from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    descripcion= models.TextField()
    image = models.ImageField(upload_to="productos/",null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    def __str__(self):
        return super().__str__()