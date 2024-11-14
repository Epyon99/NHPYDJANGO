from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from flask import redirect
from producto.forms import ProductoForm
from producto.models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.
def product_list(request):
    my_productos = Producto.objects.all()
    if my_productos.count() == 0:
        return HttpResponse("No hay productos / en general")
    return render(request, "product_list.html", {"object_list": my_productos})
    # return JsonResponse(list(my_productos.values()), safe=False)


def product_detail(request, primaryKey):
    found_producto = get_object_or_404(Producto, pk=primaryKey)
    return render(request, "product_detail.html", {"object": found_producto})


def product_create(request):
    if (request.method == 'POST'):
        form = ProductoForm(request.POST,request.FILES)
        if (form.is_valid):
            form.save()
            form = ProductoForm
            return render(request, "product_form.html", {"form": form})
    else:
        form = ProductoForm
    return render(request, "product_form.html", {"form": form})

def producto_delete(request, pk):
    del_producto = Producto.objects.filter(pk=pk)
    print (del_producto)
    if (request.method == 'POST'):
        del_producto.delete()
        return redirect('product_list')
    return render(request, "product_delete.html", {"object": del_producto})

 
class ProductoListView(ListView):
    model = Producto
    template_name = 'product_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'product_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product_form.html'
    success_url = '/productos/'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product_form.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'product_delete.html'
    success_url = '/productos/'

