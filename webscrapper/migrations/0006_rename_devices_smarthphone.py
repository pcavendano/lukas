# Generated by Django 5.0.2 on 2024-03-05 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapper', '0005_rename_getdevice_devices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Devices',
            new_name='Smarthphone',
        ),
    ]