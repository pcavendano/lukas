from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is where we configure our database schema
class websitesToScrappe(models.Model):
    url = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
    
# Nouveaux mpdels basés la response de l'API
    # Manufacturer
    # CategoryItem
    # Model

class Manufacturer(models.Model):
    manufacturer_id = models.IntegerField()
    manufacturer_code = models.CharField(max_length=20)
    manufacturer_name = models.CharField(max_length=100)

class CategoryItem(models.Model):
    item_id = models.IntegerField()
    item_order = models.IntegerField()
    item_name = models.CharField(max_length=100)

class Model(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_id = models.IntegerField()
    model_code = models.CharField(max_length=20)
    model_name = models.CharField(max_length=100)
    model_title = models.CharField(max_length=100)
    category_item = models.ForeignKey(CategoryItem, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500,default='https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ModelPrices(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='prices')
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model.name