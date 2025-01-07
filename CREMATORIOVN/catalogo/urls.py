from django.urls import path
from  .views import *

urlpatterns = [
    #LISTAR PRODUCTOS
    path('list-product/', ListProductos, name='list-product' ),
    #CREAR PRODCUTOS
    path('create-product/', CreateProduct, name='create-product'),
    #ACTUALIZAR PRODUCTO
    path('update-product/<int:id>', UpdateProduct, name='update-product'),
    #ELIMINAR PRODUCTOS
    path('delete-product/<int:id>', DeleteProduct, name='delete-product'),
]