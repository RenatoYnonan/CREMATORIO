from django.urls import path
from fallecidos.views import *

urlpatterns = [
    path('listado-fallecidos/', Fallecidos.as_view() , name='fallecidos'),
    path('listado-fallecidos/<int:pk>/', Fallecidos.as_view(), name='condolencias'),

    path('exp-fallecidos/', ReporteFallecido.as_view() , name='Excel-Fallecidos'),
]