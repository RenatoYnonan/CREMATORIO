# Generated by Django 5.1.5 on 2025-02-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_modelsurnas_product_urna'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelsurnas',
            name='descriptions_urna',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción de Urna'),
        ),
    ]
