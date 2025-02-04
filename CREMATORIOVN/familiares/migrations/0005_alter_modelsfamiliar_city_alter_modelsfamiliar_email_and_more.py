# Generated by Django 5.1.5 on 2025-02-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0004_alter_modelsfamiliar_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='city',
            field=models.CharField(max_length=155, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='gender',
            field=models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='identify_document',
            field=models.CharField(choices=[('DNI', 'DNI'), ('PST', 'PASAPORTE')], max_length=3, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='lastname',
            field=models.CharField(max_length=255, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='number_document',
            field=models.IntegerField(null=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='telephone',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]
