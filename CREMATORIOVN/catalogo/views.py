from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
def ListProductos(request):
    return render(request, 'productos/index-productos.html')
    

class ListPlanes():
    pass