from django.urls import path
from .views import *


urlpatterns = [
    path('list-proveedores', ListProveedores ,name='list-proveedores'),
    path('create-proveedores', CreateProveedores ,name='create-proveedores'),
    path('update-proveedores/<int:id>', UpdateProveedores ,name='update-proveedores'),
    path('delete-proveedores/<int:id>', DeleteProveedores ,name='delete-proveedores'),
    path('exportar-proveedores', ExportarProveedoresPDF ,name='exportar-proveedores'),
    path('exportar-proveedores-xml', ExportarProveedoresXML ,name='exportar-proveedores-xml'),
]
