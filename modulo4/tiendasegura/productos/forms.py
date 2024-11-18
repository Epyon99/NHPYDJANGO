from django import forms
from .models import Producto, Proveedor, Almacen

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['name', 'direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'descripcion', 'proveedor','image','price']

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['name', 'ubicacion', 'productos']
        widgets = {
            'productos': forms.CheckboxSelectMultiple()
        }
