from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *

from django.core.paginator import Paginator

from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms  import *

# Create your views here.
def ListProductos(request):
    product = ModelsProduct.objects.all()
    pag = Paginator(product, 8)
    page_number = request.GET.get('page')

    page_obj =  pag.get_page(page_number)


    return render(request, 'productos/index-productos.html', { 'page_obj': page_obj })


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
    

# PLANES DE CREMACION 
# - CREMACIÓN BASICA
# - CREMACION PREMIÚM 
# - PLAN A FUTURO  

def ListPlanes(request): #listar datos
    obj_plan = ModelsPlanes.objects.all()
    
    return render(request, 'planes/index-planes.html', {'obj_plan': obj_plan})

def CreatePlan(request):
    if request.method == 'POST':
        form_plan = FormPlanes(request.POST)

        if form_plan.is_valid():
            form_plan.save()
            return redirect('catalogo:list-planes')
    else: 
        form_plan = FormPlanes()


    return render(request, 'planes/index-form.html', {'form_plan': form_plan})


def UpdatePlanes(request, id):
    
    obj_planes = get_object_or_404(ModelsPlanes, id=id)

    if request.method == 'POST':
        form_plan = FormPlanes(request.POST, instance=obj_planes)

        if form_plan.is_valid():
            form_plan.save()
            return redirect('catalogo:list-planes')
    else: 
        form_plan = FormPlanes(instance=obj_planes)


    return render(request, 'planes/index-form.html', {'form_plan': form_plan})

def DeletePlanes(request, id):
    obj_planes = get_object_or_404(ModelsPlanes, id=id)

    if request.method == 'POST':

        if obj_planes.state_plan is True:
            obj_planes.state_plan = False
            obj_planes.save()
            return redirect('catalogo:list-planes')
        else:
            messages.success({f'El {obj_planes.name_plan} ya esta inactivo'})
    
    return render(request, 'planes/index-delete.html')

