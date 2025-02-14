from django.shortcuts import render, get_object_or_404
from django.views.generic import  *
from fallecidos.models import *

from django.core.paginator import Paginator

from catalogo.models import *
from blogs.models import *

from fallecidos.forms import *
from django.urls import reverse_lazy
from django.urls import reverse

from django.db.models import Q

# Create your views here.
class PaginaPrincipal(TemplateView):
    template_name = 'index-crematorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['planes'] =  ModelsPlanes.objects.prefetch_related('planes').all()
        return context

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


#PRODUCTOS Y PLANES DE CREMACION
def Tienda(request):

    categoria =  request.GET.getlist('categoria')

    urnas = []  # Inicializa las listas vacías
    planes = []

    if 'URNAS' in categoria:
        urnas = ModelsUrnas.objects.all()

    if 'PLANES' in categoria:
        planes = ModelsPlanes.objects.all()
        


    paginator =  Paginator(urnas, 6)
    num_page = request.GET.get('page')
    page_obj = paginator.get_page(num_page)

    return render(request, 'tienda/index-tienda.html', {'page_obj':  page_obj, 'planes': planes})
    


def detailsProduct(request, slug_urna):
    details_product = get_object_or_404(ModelsUrnas, slug_urna=slug_urna)
    return render(request, 'tienda/index-details-product.html', {'product': details_product})

# BLOG INFORMATIVOS

def indexblog(request):
    obj_blog  =  BlogPost.objects.all()
    return render(request, 'blogs/index-blog.html', {'blogs': obj_blog})


def detailblog(request, slug_post):
    detail_blog =  get_object_or_404(BlogPost, slug_post=slug_post)
    return render(request, 'blogs/index-details.html', {'obj_detail': detail_blog})


#CONVENIOS CON FUNDACIONES
def Convenios(request):
    return render(request, 'convenios/index-convenios.html')


#NOSOTROS
def Nosotros(request):
    return render(request, 'nosotros/index-nosotros.html')

