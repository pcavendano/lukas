from django.contrib import admin

# Register your models here.
from .models import Device, websitesToScrappe, Review, DevicePrices
admin.site.register(Device)
admin.site.register(websitesToScrappe)
admin.site.register(Review)
admin.site.register(DevicePrices)
