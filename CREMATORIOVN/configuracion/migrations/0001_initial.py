# Generated by Django 5.1.2 on 2025-01-02 20:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_social', models.CharField(choices=[('facebook', 'facebook'), ('instagram', 'instagram'), ('tiktok', 'tiktok')], max_length=10)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Redes sociales',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='CompanyConf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_conpany', models.ImageField(upload_to='Logo_company')),
                ('name_company', models.CharField(max_length=255)),
                ('address_company', models.CharField(max_length=255)),
                ('phone_company', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('social_networks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to='configuracion.socialnetworks')),
            ],
            options={
                'verbose_name': 'Configuracion Empresa',
                'verbose_name_plural': 'Configuracion Empresa',
            },
        ),
    ]
