from django.urls import path
from fallecidos.views import *

urlpatterns = [
    path('listado-fallecidos/', Fallecidos.as_view() , name='fallecidos'),
    path('listado-fallecidos/<int:pk>/', Fallecidos.as_view(), name='condolencias'),
    path('create-deceased', CreateDeceased.as_view(), name='create-deceased'),
    path('update-deceased/<int:pk>', UpdateDeceased.as_view(), name='update-deceased'),
    path('delete-deceased/<int:pk>', DeleteDeceased, name='delete-deceased'),
    #EXPORTAR DATOS  A EXCEL
    path('exp-fallecidos/', ReporteFallecido.as_view() , name='Excel-Fallecidos'),
    path('exp-fallecidos-pdf/', ReporteFallecidoPDF , name='PDF-Fallecidos'),
]