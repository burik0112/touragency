# Generated by Django 4.0 on 2021-12-17 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='email',
            new_name='messages',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='first_name',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='phone',
        ),
    ]
