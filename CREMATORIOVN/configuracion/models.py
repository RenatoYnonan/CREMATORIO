from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from django.core.exceptions import ValidationError

# Create your models here.
class SocialNetworks(models.Model):
    NAME_SOCIAL_NETWORKS = [('facebook','facebook'), ('instagram','instagram'),('tiktok','tiktok')]

    name_social = models.CharField(max_length=10, choices=NAME_SOCIAL_NETWORKS)
    url = models.URLField()

    class Meta:
        verbose_name = 'Redes sociales'
        verbose_name_plural = 'Redes Sociales'


class CompanyConf(models.Model):
    logo_conpany = models.ImageField(upload_to='Logo_company')
    name_company = models.CharField(max_length=255)
    slogan_company =  models.TextField(default='Lorem Ipsum')
    address_company =  models.CharField(max_length=255)
    gmail_company = models.EmailField(default='company@gmail.com')
    phone_company =  models.IntegerField(default=1, validators=[MinValueValidator(100000000),MaxValueValidator(9999999999)])
    social_networks = models.ForeignKey(SocialNetworks, related_name='social_networks', on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'Configuracion Empresa'
        verbose_name_plural = 'Configuracion Empresa'

    def save(self, *args, **kargs):
        limit_registers = 1

        if not self.pk and  CompanyConf.objects.count() >= limit_registers:
            raise ValidationError('No se pueden agregar mas Datos')
        return super().save(*args, **kargs)