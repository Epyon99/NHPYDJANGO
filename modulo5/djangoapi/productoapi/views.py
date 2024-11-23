from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from productoapi.models import Producto
from productoapi.serializers import ProductoModelSerializer, ProductoSerializer

# Create your views here.
class ProductoListCreateAPIView(ListCreateAPIView):
    queryset=Producto.objects.all()
    serializer_class=ProductoModelSerializer

class ProductoRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer