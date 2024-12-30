from django.db import models

# Create your models here.
class ModelsInstitucion(models.Model):
    foto_institucion =  models.ImageField(upload_to='Fotos Instituciones')
    nombre_institucion =  models.CharField(max_length=255)
    ciudad = models.CharField(max_length=155)
    redes_sociales = models.URLField()
    estado = models.BooleanField(default=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class ModelsFunerarias(models.Model):
    foto_funeraria =  models.ImageField(upload_to='Fotos Funerarias')
    nombre_funeraria =  models.CharField(max_length=255)
    ciudad = models.CharField(max_length=155)
    redes_sociales = models.URLField()
    estado = models.BooleanField(default=True)
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Funeraria'
        verbose_name_plural = 'Funerarias'

