# Generated by Django 5.1.2 on 2024-12-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallecidos', '0007_alter_fallecido_documento_identidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fallecido',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1),
        ),
    ]
