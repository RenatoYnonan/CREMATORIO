from django.urls import path
from .views import *

urlpatterns = [
    #INSTITUCIONES
    path('list-instituciones/', ListInstituciones.as_view(), name='list-instituciones' ),
    path('list-instituciones/delete/<int:id>', DeleteInstitucion , name='delete-instituciones'),

    #FUNERARIAS
    path('list-funerarias/', ListFunerarias.as_view(), name='list-funerarias' ),
    path('delete/<int:id>/', deleteFuneraria, name='delete-funeraria'),
    path('create-funeraria/', CreateFuneraria, name='create-funeraria'),
    path('update-funeraria/<int:id>/', UpdateFuneraria, name='update-funeraria'),
    path('exportar-funerarias-xml/', ExportarFunerariasXML, name='exportar-funerarias-xml'),
    path('exportar-funerarias-pdf/', ExportarFunerariasPDF, name='exportar-funerarias-pdf'),
]