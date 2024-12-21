from django.urls import path
from .views import *


urlpatterns =[
    path('', PaginaPrincipal.as_view(), name='crematorio'),
    path('mural-de-recuerdo/', MuralRecuerdo.as_view(), name='recuerdos'),
    path('mural-condolencias/<int:id>', MuralCondolencias.as_view(), name='condolencia'),
    path('create-condolencias/<int:id>', CreateCondolencias.as_view(), name='crear-condolencias')
]