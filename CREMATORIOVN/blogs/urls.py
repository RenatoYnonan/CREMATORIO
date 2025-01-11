from django.urls import path
from .views import *

urlpatterns =[
    path('list-blogs', ListBlog , name='list-blogs')
]