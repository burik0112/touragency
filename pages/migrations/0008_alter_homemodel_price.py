# Generated by Django 4.0 on 2021-12-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_homemodel_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='price',
            field=models.TextField(max_length=50, verbose_name='price'),
        ),
    ]