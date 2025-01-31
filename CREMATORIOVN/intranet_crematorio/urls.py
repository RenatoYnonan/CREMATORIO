from django.urls import path
from intranet_crematorio.views import *
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('', Intranet.as_view(), name='intranet'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
]

