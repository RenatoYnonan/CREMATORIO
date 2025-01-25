from django.urls import path
from .views import EmailIndex


urlpatterns = [
    path('', EmailIndex.as_view(), name='email_index'),
]
