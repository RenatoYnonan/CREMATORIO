from django.urls import path
from intranet_crematorio.views import *

urlpatterns= [
    path('intranet/', Intranet.as_view(), name='intranet')
]

