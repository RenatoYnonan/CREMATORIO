from os import error
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import *

from django.urls import reverse_lazy
from .forms import *

from django.views.generic import *

# Create your views here.
def ListBlog(request):
    obj_blog =  BlogPost.objects.all()
    paginator =  Paginator(obj_blog, 6)

    num_page = request.GET.get('page')
    page_obj = paginator.get_page(num_page)

    return render(request, 'index-blog.html', {'page_obj':  page_obj})

class CreateBlog(CreateView):
    model =  BlogPost
    form_class =  FormBlog
    template_name =  'index-form-blog.html'
    success_url =  reverse_lazy('blogs:list-blogs')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateBlog(UpdateView):   
    model =  BlogPost
    form_class =  FormBlog
    template_name =  'index-form-blog.html'
    success_url =  reverse_lazy('blogs:list-blogs')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


def DeleteBlog(request, pk):
    obj_blog =  BlogPost.objects.get(pk=pk)
    if request.method == 'POST':
        if obj_blog.is_published == True:
            obj_blog.is_published = False
            obj_blog.save()
            return redirect('blogs:list-blogs')
        else:
            obj_blog.is_published = True
            obj_blog.save()
            return redirect('blogs:list-blogs')
            
    return render(request, 'index-delete-blog.html', {'obj_blog': obj_blog})

    