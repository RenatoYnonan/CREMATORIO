# Generated by Django 5.1.2 on 2025-01-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyconf',
            name='gmail_company',
            field=models.EmailField(default='company@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='companyconf',
            name='slogan_company',
            field=models.TextField(default='Lorem Ipsum'),
        ),
    ]
