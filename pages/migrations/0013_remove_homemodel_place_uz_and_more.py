# Generated by Django 4.0 on 2022-01-13 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_homemodel_place_en_homemodel_place_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homemodel',
            name='place_uz',
        ),
        migrations.RemoveField(
            model_name='homemodel',
            name='remains_uz',
        ),
        migrations.RemoveField(
            model_name='homemodel',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='placemodel',
            name='price_uz',
        ),
        migrations.RemoveField(
            model_name='placemodel',
            name='title_uz',
        ),
    ]
