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
    name_product = models.CharField(max_length=155,  verbose_name='Nombre Producto')
    descriptions_product = models.TextField(verbose_name='Descripción de Producto')
    price_product =  models.FloatField(verbose_name='Precio Producto')
    stock_product = models.IntegerField()
    planes =  models.ManyToManyField(ModelsPlanes, related_name='planes' )
    state_product = models.BooleanField(default=True)
    slug_product = models.SlugField(max_length=255, unique=True, blank=True)
    date_create_product = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_product
    
    def save(self, *args, **kwargs):
        if not self.slug_product:
            self.slug_product = slugify(self.name_product)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'


class ModelsUrnas(models.Model):
    MATERIALES = [('METAL', 'METAL'), ('MADERA', 'MADERA'), ('MARMOL', 'MARMOL')]


    material_urna =  models.CharField(max_length=10, choices=MATERIALES, default='MADERA', verbose_name='Material Urna')
    nombre_urna = models.CharField(max_length=255, verbose_name='Nombre Urna')
    descriptions_urna = models.TextField(verbose_name='Descripción de Urna', blank=True, null=True)
    price_urna = models.FloatField(verbose_name='Precio Urna')
    stock_urna = models.IntegerField()
    state_urna = models.BooleanField(default=True)
    product_urna =  models.ForeignKey(ModelsProduct, on_delete=models.CASCADE, related_name='urnas', null=True)
    slug_urna = models.SlugField(max_length=255, unique=True, blank=True)
    date_create_urna = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_urna
    
    def save(self, *args, **kwargs):
        if not self.slug_urna:
            self.slug_urna = slugify(self.nombre_urna)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Urna'
        verbose_name_plural = 'Urnas'