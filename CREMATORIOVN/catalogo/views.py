from django.shortcuts import render, redirect
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
    

class ListPlanes():
    pass