from tabnanny import verbose
from django.db import models

# Create your models here.
class ModelsFamiliar(models.Model):
    GENERO_FAMILIAR = [ ('M', 'MASCULINO'), ('F', 'FEMENINO')]
    DOCUMENTO_IDENTIDAD = [('DNI', 'DNI'), ('PST', 'PASAPORTE')]

    name =  models.CharField(max_length=255, verbose_name='Nombre')
    lastname = models.CharField(max_length=255, verbose_name='Apellido')
    telephone =  models.IntegerField(verbose_name='Telefono')
    email =  models.EmailField(max_length=255, verbose_name='Email')
    city = models.CharField(max_length=155, verbose_name='Ciudad')
    gender = models.CharField(max_length=1, choices=GENERO_FAMILIAR, verbose_name='Genero')
    identify_document =  models.CharField(max_length=3, choices=DOCUMENTO_IDENTIDAD, verbose_name='Tipo de documento')
    number_document =  models.IntegerField(null=True, verbose_name='Número de documento')
    estado =  models.BooleanField( max_length=150 ,default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Familiare'
        verbose_name_plural = 'Familiares'
