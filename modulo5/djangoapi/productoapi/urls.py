from django.urls import path
from .views import ProductoListCreateAPIView, ProductoRUDAPIView
from productoapi import views

urlpatterns = [
    path('productos/',ProductoListCreateAPIView.as_view(),name="product_list"),
    path('productos/manage',ProductoRUDAPIView.as_view(),name='producto_manage')

]
