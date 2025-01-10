from django.shortcuts import render, get_object_or_404
from django.views.generic import  *
from fallecidos.models import *

from django.core.paginator import Paginator

from catalogo.models import *

from fallecidos.forms import *
from django.urls import reverse_lazy
from django.urls import reverse

# Create your views here.
class PaginaPrincipal(TemplateView):
    template_name = 'index-crematorio.html'


class MuralRecuerdo(ListView):
    model = Fallecido
    context_object_name = 'fallecido'
    template_name = 'index-mural.html'

class MuralCondolencias(CreateView):
    model = Condolencias
    form_class = CondolenciaForms
    context_object_name = 'fallecido'
    template_name = 'index-condolencias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fallecido_id =  self.kwargs.get('id')
        context['condolencias'] =  Condolencias.objects.filter(nombre_fallecido_id =  fallecido_id)
        context['fc'] =  get_object_or_404(Fallecido, id=fallecido_id)

        return context


class CreateCondolencias(CreateView):
    model = Condolencias
    form_class = CondolenciaForms
    template_name = 'formularios/index-form-condolencias.html'

    def form_valid(self, form):
        fallecido_id =  self.kwargs.get('id')
        fallecido = get_object_or_404(Fallecido, id=fallecido_id)

        form.instance.nombre_fallecido = fallecido
        return super().form_valid(form)
    
    def get_success_url(self):
        fallecido_id = self.kwargs.get('id')
        return reverse('condolencia', kwargs={'id': fallecido_id})
        

# def MuralCondolencias(request, id):
#     fallecido =  Fallecido.objects.filter(id=id).first()
#     cn =  Condolencias.objects.filter(nombre_fallecido_id = fallecido.id)  
#     return render(request, 'index-condolencias.html', { 'condolencias': cn, 'falledico': fallecido})


def Tienda(request):
    urnas =  ModelsProduct.objects.filter(category_product = 'URNAS')

    paginator =  Paginator(urnas, 6)
    num_page = request.GET.get('page')
    page_obj = paginator.get_page(num_page)

    return render(request, 'tienda/index-tienda.html', {'page_obj':  page_obj})


def detailsProduct(request, slug_product):
    details_product = get_object_or_404(ModelsProduct, slug_product=slug_product)
    return render(request, 'tienda/index-details-product.html', {'product': details_product})

