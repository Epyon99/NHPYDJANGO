from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from .forms import ProveedorForm, ProductoForm, AlmacenForm
from .models import Almacen, Producto, Proveedor
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

def create_almacen(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('almacen/almacen_list')
    else:
        form = AlmacenForm()
    return render(request, 'almacen/almacen_create.html', {'form': form})

def edit_almacen(request, almacen_id):
    almacen = get_object_or_404(Almacen, id=almacen_id)
    if request.method == 'POST':
        form = AlmacenForm(request.POST, instance=almacen)
        if form.is_valid():
            form.save()
            return redirect('almacen/almacen_list')
    else:
        form = AlmacenForm(instance=almacen)
    return render(request, 'almacen/almacen_edit.html', {'form': form, 'almacen': almacen})

class ProductoListView(PermissionRequiredMixin,ListView):
    model = Producto
    template_name = 'producto/product_list.html'
    permission_required = 'productos.view_producto'
    login_url = '/accounts/login/' # Donde autenticarse

class ProductoView(DetailView):
    model = Producto
    template_name = 'producto/product_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/product_form.html'
    success_url = '/productos/'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/product_form.html'
    success_url = '/productos/'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/product_delete.html'
    success_url = '/productos/'

class ProveedoresClassView(View):
    def get(self, request, proveedor_id=None):
        if proveedor_id:
            proveedor = get_object_or_404(Proveedor, id=proveedor_id)
            form =ProveedorForm(instance=proveedor)
            return render(request,'proveedor_form.html', {'form':form})
        else:
            form =ProveedorForm()
            return render(request,'proveedor/proveedor_form.html',{'form':form})
    def post(self,request):
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_listview')
        else:
            return render(request,'proveedor_form.html',{'form':form})