# Generated by Django 5.1.5 on 2025-01-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedoresmodels',
            name='description',
        ),
        migrations.AddField(
            model_name='proveedoresmodels',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]
