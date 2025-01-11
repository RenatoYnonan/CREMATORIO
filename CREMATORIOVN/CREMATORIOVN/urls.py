"""
URL configuration for CREMATORIOVN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('base.urls')),
    path('intranet-crematorio/', include(('intranet_crematorio.urls', 'intranet_crematorio'), namespace='intranet-crematorio')),
    path('fallecidos/', include(('fallecidos.urls', 'fallecidos'), namespace='fallecidos')),
    path('familiares/', include(('familiares.urls', 'familiares'), namespace='familiares')),
    path('convenios/', include(('convenios.urls', 'convenios'), namespace='convenios')),
    path('admin/', admin.site.urls),
    #DATOS DE EMPRESA
    path('empresa/', include(('configuracion.urls', 'configuracion'), namespace='empresa')),

    #CATALOGO DE PRODUCTOS
    path('catalogo/', include(('catalogo.urls', 'catalogo'), namespace='catalogo')),

    #BLOGS POST
    path('blogs/', include(('blogs.urls', 'blogs'), namespace='blogs')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

