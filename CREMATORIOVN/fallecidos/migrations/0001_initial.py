# Generated by Django 5.1.4 on 2024-12-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fallecido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=155)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_fallecido', models.DateField()),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('documento_identidad', models.CharField(choices=[('DNI', 'Documento de Identidad'), ('PST', 'Pasaporte')], max_length=3)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
