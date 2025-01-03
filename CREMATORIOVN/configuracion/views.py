from django.shortcuts import render
from django.views.generic import *

from django.shortcuts import redirect


from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

class ConfiguracionEmpresa(UpdateView):
    model = CompanyConf
    form_class = FormCompany
    template_name = 'index-empresa.html'
    success_url = reverse_lazy('configuracion:config-company', kwargs = { 'pk':1 })
