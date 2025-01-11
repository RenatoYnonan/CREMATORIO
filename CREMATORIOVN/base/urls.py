from django.urls import path
from .views import *


urlpatterns =[
    path('', PaginaPrincipal.as_view(), name='crematorio'),
    path('mural-de-recuerdo/', MuralRecuerdo.as_view(), name='recuerdos'),
    path('mural-condolencias/<int:id>', MuralCondolencias.as_view(), name='condolencia'),
    path('create-condolencias/<int:id>', CreateCondolencias.as_view(), name='crear-condolencias'),

    #TIENDA
    path('store/', Tienda, name='store'),
    # Detalles de producto
    path('details/<slug:slug_product>', detailsProduct ,name='details-product'),

    #BLOGS
    path('blogs', indexblog, name='blogs'),
    path('detail-blog/<slug:slug_post>/', detailblog, name='detail-blog'),
]