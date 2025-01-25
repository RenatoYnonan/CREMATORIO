from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class EmailIndex(LoginRequiredMixin, TemplateView):
    template_name = 'email/index-email.html'
    login_url = 'intranet-crematorio:login'

