from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
# Create your views here.

class Intranet(LoginRequiredMixin,TemplateView):
    login_url = 'intranet-crematorio:login'
    template_name = 'index.html'

class Login(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('intranet-crematorio:intranet')
        return super().dispatch(request, *args, **kwargs)
