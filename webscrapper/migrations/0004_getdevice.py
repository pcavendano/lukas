# Generated by Django 5.0.2 on 2024-03-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapper', '0003_websitestoscrappe_deviceprices_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='getDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]