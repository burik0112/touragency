# Generated by Django 3.2.8 on 2021-11-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tourmodel_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourmodel',
            old_name='img1',
            new_name='image',
        ),
    ]
