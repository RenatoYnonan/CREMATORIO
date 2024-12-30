from django.shortcuts import render
from django.views.generic import *
from .models import *
from openpyxl  import Workbook
from openpyxl.styles import Alignment
from django.http import HttpResponse
import datetime


class ReporteFallecido(TemplateView):
    def get(self, request, *args, **kwargs):
        exfallecido =  Fallecido.objects.all()

        wb  = Workbook()
        ws = wb.active

        ws['B1'] = 'LISTADO DE FALLECIDOS'
        ws['B1'].alignment = Alignment(horizontal='center', vertical='center')
        ws.merge_cells('B1:E1')

        ws['B3'] = 'NOMBRE'
        ws['C3'] = 'APELLIDO'
        ws['D3'] = 'FECHA DE NACIMIENTO'
        ws.column_dimensions['D'].width = 22
        ws['E3'] = 'FECHA DE FALLECIDO'
        ws.column_dimensions['E'].width = 22
        ws['F3'] = 'GENERO'
        ws['G3'] = 'DNI'
        
        contador = 4

        for i in exfallecido:
            ws.cell(row=contador, column=2).value = i.nombre_completo.capitalize()
            ws.cell(row=contador, column=3).value = i.apellido.capitalize()

            #FECHA DE NACIMIENTO
            ws.cell(row=contador, column=4).value = i.fecha_nacimiento
            ws.cell(row=contador, column=4).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

            #FECHA DE FALLECIDO
            ws.cell(row=contador, column=5).value = i.fecha_fallecido
            ws.cell(row=contador, column=5).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)


            ws.cell(row=contador, column=6).value = i.get_genero_display()
            ws.cell(row=contador, column=7).value = i.documento_identidad
        
            contador += 1

        Reporte_Fallecido = "Crematorio_Reporte_Fallecido.xlsx"
        response = HttpResponse(content_type = "aplication/ms-excel")
        content = "attachment; filename = {0}".format(Reporte_Fallecido)
        response['Content-Disposition'] = content
        wb.save(response)

        return response



class Fallecidos(ListView):
    model = Fallecido
    context_object_name = 'fallecidos'
    template_name = 'index_fallecido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fallecido_id = self.kwargs.get('pk')
        if fallecido_id: 
            context['condolencias'] = Condolencias.objects.filter(nombre_fallecido_id=fallecido_id)
            context['count'] =  Condolencias.objects.count()
        else:
            context['condolencias'] = None

        return context


    
    
