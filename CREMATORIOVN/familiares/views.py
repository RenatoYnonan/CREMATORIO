from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from openpyxl import Workbook
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
class ListFamily(TemplateView):
    template_name = 'index-familiar.html'

    def get(self, request, *args, **kwargs):
        familiares = ModelsFamiliar.objects.all()
        form = FamiliaresForms()
        return render(request, self.template_name, {
            'familiares': familiares,
            'form': form
        })
    

    def post(self, request, *args, **kwargs):
        form = FamiliaresForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('familiares:list-familiares'))  

        familiares = ModelsFamiliar.objects.all()
        return render(request, self.template_name, {
            'familiares': familiares,
            'form': form
        })
    

class FamiliarUpdate(UpdateView):
    model = ModelsFamiliar
    form_class = FamiliaresForms
    template_name = 'index-form-familiar.html'
    success_url =  reverse_lazy('familiares:list-familiares')
    


class ReporteExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        exfami = ModelsFamiliar.objects.all()
        wb = Workbook()
        ws = wb.active
        ws['B1'] = 'REPORTE DE FAMILIARES'

        ws.merge_cells('B1:E1')
        ws['B3'] = 'NOMBRES'
        ws['C3'] = 'APELLIDOS'

        contador = 2

        for i in exfami:
            ws.cell(row=contador, column=2).value = i.name.capitalize()
            ws.cell(row=contador, column=3).value = i.lastname.capitalize()

            contador += 1
        
        Reporte_Familiares = "Crematorio_Reporte_Familiares.xlsx"
        response = HttpResponse(content_type = "aplication/ms-excel")
        content = "attachment; filename = {0}".format(Reporte_Familiares)
        response['Content-Disposition'] = content
        wb.save(response)

        return response