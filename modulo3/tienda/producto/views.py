from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from producto.models import Marca, MarcaProducto, Producto

# Create your views here.
def product_list(request):
    my_productos = Producto.objects.all()
    if (my_productos.count() == 0):
        return HttpResponse("No hay productos / en general")
    return render(request, 'product_list.html', {'productos': my_productos})
    #return JsonResponse(list(my_productos.values()), safe=False)

def product_detail(request, primaryKey):
    found_producto = get_object_or_404(Producto, pk=primaryKey)
    return render(request, 'product_detail.html', {'producto': found_producto})

def mixto(request):
    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    mixtos = MarcaProducto()
    mixtos.listaProductos = productos
    mixtos.listaMarcas = marcas
    return render(request, 'product_detail.html', {'mixtos': mixtos})