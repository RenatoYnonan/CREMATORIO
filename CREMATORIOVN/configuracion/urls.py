from django.urls import path
from .views import *

urlpatterns = [
    path('config-company/<int:pk>', ConfiguracionEmpresa.as_view(), name='config-company')
]