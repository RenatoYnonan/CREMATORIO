from django.shortcuts import render
from django.views.generic import *
# Create your views here.

class Intranet(TemplateView):
    template_name = 'index.html'