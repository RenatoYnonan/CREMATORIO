from django.urls import path
from intranet_crematorio.views import *
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('intranet/', Intranet.as_view(), name='intranet'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

