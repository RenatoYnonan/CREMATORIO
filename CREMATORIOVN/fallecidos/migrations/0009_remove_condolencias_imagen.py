# Generated by Django 5.1.2 on 2024-12-20 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fallecidos', '0008_alter_fallecido_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condolencias',
            name='imagen',
        ),
    ]
