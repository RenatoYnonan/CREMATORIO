from django.db import models
from django.utils import timezone

# Create your models here.




class Fallecido(models.Model):
    GENERO = [('F', 'Femenino'), ('M', 'Masculino')]
    DOCUMENTO = [('DNI', 'Documento de Identidad'), ('PST', 'Pasaporte')]

    nombre_completo = models.CharField(max_length=255)
    apellido = models.CharField(max_length=155)
    fecha_nacimiento = models.DateField()
    fecha_fallecido = models.DateField()
    genero =  models.CharField(choices=GENERO, max_length=1, default='M')
    documento_identidad =  models.CharField(choices=DOCUMENTO,max_length=3, default='DNI')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Condolencias(models.Model):
    nombre_fallecido = models.ForeignKey(Fallecido, on_delete=models.CASCADE, related_name='fallecido')
    # imagen = models.ImageField(upload_to='Fotos Condolencias')
    descripcion = models.CharField(max_length=255)
    nombre_familiar = models.CharField(max_length=155)
    fecha_creacion = models.DateTimeField(default=timezone.now, null=False, blank=False)