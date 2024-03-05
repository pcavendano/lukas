from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is where we configure our database

class getDevice(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField()
    description = models.TextField()
    def __str__(self):
        return self.name