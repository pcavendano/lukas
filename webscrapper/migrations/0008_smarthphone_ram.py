# Generated by Django 5.0.2 on 2024-03-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapper', '0007_smarthphone_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='smarthphone',
            name='ram',
            field=models.IntegerField(default=16, verbose_name=16),
            preserve_default=False,
        ),
    ]