from django.urls import path
from .views import *

urlpatterns = [
    path('listar-familiares/', ListFamily.as_view() , name='list-familiares'),
    path('update-familiares/<int:pk>', FamiliarUpdate.as_view() , name='update-familiares'),
]