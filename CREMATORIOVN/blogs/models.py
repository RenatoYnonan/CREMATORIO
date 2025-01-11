from django.db import models
from django.utils.text import  slugify
from tinymce.models import HTMLField


# Create your models here.
class BlogPost(models.Model):
    image_post = models.ImageField(verbose_name='Imagen', upload_to='Imagenes Blogs')
    title_post = models.CharField(max_length=255, verbose_name='Titulo Post')
    descriptions_post = models.TextField()
    content_post = HTMLField(verbose_name='Contenido')
    date_create = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    slug_post = models.SlugField(unique=True, blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Estado Publicación')

    def __str__(self):
        return super().__str__()
    
    def save(self, *args, **kwargs):

        if not self.slug_post:
            self.slug_post = slugify(self.title_post)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'