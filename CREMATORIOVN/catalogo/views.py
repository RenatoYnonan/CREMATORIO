from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *

from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms  import *

# Create your views here.
def ListProductos(request):
    product = ModelsProduct.objects.all()
    return render(request, 'productos/index-productos.html', { 'productos': product })


def CreateProduct(request):

    if request.method == 'POST':
        form = FormsProduct(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogo:list-product')
    else:
        form = FormsProduct()
    return render(request, 'productos/index-form.html', { 'form': form })


def UpdateProduct(request, id):
    datos = get_object_or_404(ModelsProduct, id=id)

    if request.method == 'POST':
        form = FormsProduct(request.POST, instance=datos)

        if form.is_valid():
            form.save()
            return redirect('catalogo:list-product')
    else:
        form = FormsProduct(instance=datos)


    return render(request, 'productos/index-form.html', {'form': form})


def DeleteProduct(request, id):
    data = get_object_or_404(ModelsProduct, id=id)

    if request.method == 'POST':
        data.state_product = False
        data.save()
        return redirect('catalogo:list-product')
    else:
        form = FormsProduct(instance=data)
    
    return render(request, 'productos/index-delete.html', {'form': form})
    
    

class ListPlanes():
    pass