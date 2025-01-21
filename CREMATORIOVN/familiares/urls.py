from django.urls import path
from .views import *

urlpatterns = [
    path('listar-familiares/', ListFamily.as_view() , name='list-familiares'),
    path('update-familiares/<int:pk>', FamiliarUpdate.as_view() , name='update-familiares'),
    path('create-familiares/', CreateFamiliar , name='create-familiares'),
    path('delete-familiares/<int:pk>', DeleteFamiliar , name='delete-familiares'),
    path('export-familiares/', ReporteExcel.as_view() , name='export-familiares'),
    path('pdf-familiares/', ReportePDF , name='pdf-familiares'),
]