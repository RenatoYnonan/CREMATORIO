from django.shortcuts import render
from django.views.generic import *
from .models import *



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


    
    
