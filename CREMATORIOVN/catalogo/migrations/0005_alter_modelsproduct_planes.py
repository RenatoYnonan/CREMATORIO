# Generated by Django 5.1.2 on 2025-01-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_remove_modelsproduct_planes_modelsproduct_planes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsproduct',
            name='planes',
            field=models.ManyToManyField(null=True, related_name='planes', to='catalogo.modelsplanes'),
        ),
    ]
