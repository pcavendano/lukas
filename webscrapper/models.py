from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is where we configure our database

class websitesToScrappe(models.Model):
    url = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    memory = models.IntegerField()
    image = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class DevicePrices(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='prices')
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name
    
class Smarthphone(models.Model):
    names = models.CharField(max_length=100)
    prix = models.FloatField()
    def __str__(self):
        return self.name