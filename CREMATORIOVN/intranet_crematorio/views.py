from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Intranet(LoginRequiredMixin,TemplateView):
    login_url = '/admin/'
    template_name = 'index.html'
