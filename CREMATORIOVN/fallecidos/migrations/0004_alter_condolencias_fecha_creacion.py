# Generated by Django 5.1.2 on 2024-12-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallecidos', '0003_condolencias_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condolencias',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
