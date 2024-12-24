from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from django.http import HttpResponseRedirect

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
    
    