from django.db import models
from django.shortcuts import HttpResponse

from django.utils.text import slugify

# Create your models here.

class ModelsPlanes(models.Model):
    name_plan = models.CharField(max_length=255, unique=True, verbose_name='Nombre Plan')
    description_plan = models.TextField(verbose_name='Descripción del Plan')
    price_plan = models.FloatField(verbose_name='Precio Plan')
    state_plan = models.BooleanField(default=True)
    date_create_plan = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_plan

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

class ModelsProduct(models.Model):
    CATEGORY_PRODUCT = [('URNAS', 'URNAS' ), ('IMPLEMENTOS', 'IMPLEMENTOS')]


    name_product = models.CharField(max_length=155,  verbose_name='Nombre Producto')
    descriptions_product = models.TextField(verbose_name='Descripción de Producto')
    price_product =  models.FloatField(verbose_name='Precio Producto')
    category_product = models.CharField(max_length=15, choices=CATEGORY_PRODUCT,verbose_name='Categoria de producto', default='IMPLEMENTOS')
    stock_product = models.IntegerField()
    planes =  models.ManyToManyField(ModelsPlanes, related_name='planes' )
    state_product = models.BooleanField(default=True)
    slug_product = models.SlugField(max_length=255, unique=True, blank=True)
    date_create_product = models.DateField(auto_now_add=True)

    def __str__(self, *args, **kargs):
        return self.name_product
    
    def save(self, *args, **kwargs):
        if not self.slug_product:
            self.slug_product = slugify(self.name_product)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'

