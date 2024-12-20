from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name','descripcion','price' \
                  ,'image', 'is_deleted']
        
class ProductoProveedorForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name','descripcion','price','proveedor']
        widgets = {
            'proveedor': forms.HiddenInput()
        }
