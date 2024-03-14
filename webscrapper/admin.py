from django.contrib import admin

# Register your models here.
from .models import WebsitesToScrappe, ModelPrice, Manufacturer, CategoryItem, Model, RepairPrices
admin.site.register(WebsitesToScrappe)
admin.site.register(ModelPrice)
admin.site.register(RepairPrices)
# Nouveaux mpdels basés la response de l'API
    # Manufacturer
    # CategoryItem
    # Model
admin.site.register(Manufacturer)
admin.site.register(CategoryItem)
admin.site.register(Model)
# Path: webscrapper/api/urls.py
# Compare this snippet from webscrapper/views.py:
