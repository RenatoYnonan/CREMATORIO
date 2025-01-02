from django.shortcuts import render
from django.views.generic import *
from .models import *

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

class ListInstituciones(ListView):
    model = ModelsInstitucion
    context_object_name = 'instituciones'
    template_name = 'instituciones/index-instituciones.html'


class ListFunerarias(ListView):
    model = ModelsFunerarias
    context_object_name = 'funerarias'
    template_name = 'funerarias/index-funerarias.html'


class DeleteInstitucion(TemplateView):
    template_name = 'instituciones/index-delete.html'

    def get(self, request, id):
        institucion =  ModelsInstitucion.objects.filter(pk=id).first()

        return render(request, 'instituciones/index-delete.html')
    
    def post(self, request, id):
        
        institucion =  ModelsInstitucion.objects.filter(pk=id).first()
        institucion.estado = False
        institucion.save()
        return redirect('convenios:list-instituciones')

        


def deleteFuneraria(request, id):
    funeraria = get_object_or_404(ModelsFunerarias, pk=id)

    if request.method == 'GET': 
        return render(request, 'funerarias/index-delete.html')

    if request.method == 'POST':  
        funeraria.estado = False  
        funeraria.save()
        return redirect('convenios:list-funerarias')
    
    return HttpResponseNotAllowed(['POST'])