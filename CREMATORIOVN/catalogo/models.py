from django.db import models

# Create your models here.

class ModelsProduct():
    name_product = models.CharField(max_length=155, verbose_name='Nombre Producto')
    descriptions_product = models.TextField(verbose_name='Descripción de Producto')
    price_product =  models.FloatField(verbose_name='Precio Prodcuto')
    stock_product = models.IntegerField()
    state_product = models.BooleanField()
    date_create_product = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'

class ModelsPlanes():
    name_plan = models.CharField(max_length=255, verbose_name='Nombre Plan')
    description_plan = models.TextField(verbose_name='Descripción del Plan')
    price_plan = models.FloatField(verbose_name='Precio Plan')
    state_plan = models.BooleanField()
    date_create_plan = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'