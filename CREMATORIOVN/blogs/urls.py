from django.urls import path
from .views import *

urlpatterns =[
    path('list-blogs', ListBlog , name='list-blogs'),
    path('create-blogs', CreateBlog.as_view() , name='create-blogs'),
    path('update-blogs/<int:pk>', UpdateBlog.as_view() , name='update-blogs'),
    path('delete-blogs/<int:pk>', DeleteBlog , name='delete-blogs'),
]