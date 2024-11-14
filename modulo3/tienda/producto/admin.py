from django.contrib import admin
from producto.models import Producto
from .models import Proveedor

# Register your models here.
admin.site.register(Producto)
admin.site.register(Proveedor)