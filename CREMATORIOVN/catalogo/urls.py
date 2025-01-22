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
    #EXPORTAR DATOS A PDF
    path('exportar-productos-pdf/', exportar_pdf, name='exportar_productos_pdf'),
    #EXPORTAR DATOS A XML
    path('exportar-productos-xml/', ExportarXML, name='exportar_productos_xml'),


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
    path('exportar-planes-pdf/', ExportarPlanesPdf, name='exportar_planes_pdf'),
    #EXPORTAR DATOS A XML
    path('exportar-planes-xml/', ExportarPlanesXML, name='exportar_planes_xml'),
]