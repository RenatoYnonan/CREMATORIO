from django.urls import path
from .views import *

urlpatterns = [
    path('list-instituciones/', ListInstituciones.as_view(), name='list-instituciones' ),

    path('list-instituciones/delete/<int:id>', DeleteInstitucion.as_view() , name='delete-instituciones'),

    #FUNERARIAS
    path('list-funerarias/', ListFunerarias.as_view(), name='list-funerarias' ),
    path('delete/<int:id>/', deleteFuneraria, name='delete-funeraria')
]