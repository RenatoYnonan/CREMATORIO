# Generated by Django 5.1.2 on 2025-01-03 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_remove_companyconf_social_networks'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetworks',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to='configuracion.companyconf'),
        ),
    ]