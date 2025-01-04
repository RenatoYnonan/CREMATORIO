from django.urls import path
from  .views import *

urlpatterns = [
    path('list-product/', ListProductos, name='list-product' ),
    path('create-product/', CreateProduct, name='create-product')
]