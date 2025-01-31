# Generated by Django 5.1.2 on 2024-12-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('city', models.CharField(max_length=155)),
                ('gender', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1)),
                ('identify_document', models.CharField(max_length=3)),
                ('estado', models.CharField(default=True, max_length=150)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
