# Generated by Django 5.0.2 on 2024-03-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapper', '0017_alter_modelprice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelprice',
            name='model_code',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
