from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class ConfiguracionEmpresa(TemplateView):
    template_name = 'index-empresa.html'
    