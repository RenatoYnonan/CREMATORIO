from django.db import models

# Create your models here.
class ModelsFamiliar(models.Model):
    GENERO_FAMILIAR = [ ('M', 'MASCULINO'), ('F', 'FEMENINO')]
    DOCUMENTO_IDENTIDAD = [('DNI', 'DNI'), ('PST', 'PASAPORTE')]

    name =  models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telephone =  models.IntegerField()
    email =  models.EmailField(max_length=255)
    city = models.CharField(max_length=155)
    gender = models.CharField(max_length=1, choices=GENERO_FAMILIAR)
    identify_document =  models.CharField(max_length=3, choices=DOCUMENTO_IDENTIDAD)
    number_document =  models.IntegerField(null=True)
    estado =  models.BooleanField( max_length=150 ,default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Familiare'
        verbose_name_plural = 'Familiares'
