from django.urls import path
from  .views import *

urlpatterns = [
    #PRODUCTOS
    #LISTAR PRODUCTOS
    path('list-product/', ListProductos, name='list-product' ),
    #CREAR PRODCUTOS
    path('create-product/', CreateProduct, name='create-product'),
    #ACTUALIZAR PRODUCTO
    path('update-product/<int:id>', UpdateProduct, name='update-product'),
    #ELIMINAR PRODUCTOS
    path('delete-product/<int:id>', DeleteProduct, name='delete-product'),

    #PLANES DE CREMACION

    # LISTAR PLANES
    path('list-planes-cremacion/', ListPlanes, name='list-planes'),
    #CREAR PLANES
    path('create-planes-cremacion/', CreatePlan, name='create-planes'),
    #ACTUALIZAR PLANES
    path('update-planes-cremacion/<int:id>/', UpdatePlanes, name='update-planes'),
    #ELIMINAR PLANES
    path('delete-planes-crematorio/<int:id>/', DeletePlanes, name='delete-planes'),


    #EXPORTAR DATOS A PDF
    path('exportar-pdf/', exportar_pdf, name='exportar_pdf'),

]