# Generated by Django 5.1.5 on 2025-01-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image_post',
            field=models.ImageField(blank=True, null=True, upload_to='Imagenes Blogs', verbose_name='Imagen'),
        ),
    ]
