from django.db import models

# Create your models here.
class ProveedoresModels(models.Model):
    name_proveedores = models.CharField(max_length=255)
    telephone =  models.IntegerField()
    ocupation =  models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    hours_work = models.CharField(max_length=155)
    date_add = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


        