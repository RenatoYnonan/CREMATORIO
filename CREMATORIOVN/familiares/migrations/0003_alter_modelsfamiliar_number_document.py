# Generated by Django 5.1.2 on 2024-12-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_alter_modelsfamiliar_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelsfamiliar',
            name='number_document',
            field=models.IntegerField(),
        ),
    ]
