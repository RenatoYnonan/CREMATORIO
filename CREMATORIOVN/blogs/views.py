from django.shortcuts import render
from .models import *


# Create your views here.
def ListBlog(request):
    obj_blog =  BlogPost.objects.all()
    return render(request, 'index-blog.html', {'obj_blog': obj_blog})