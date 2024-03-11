from django.contrib import admin

# Register your models here.
from .models import websitesToScrappe, ModelPrices, Manufacturer, CategoryItem, Model
admin.site.register(websitesToScrappe)
admin.site.register(ModelPrices)
# Nouveaux mpdels basés la response de l'API
    # Manufacturer
    # CategoryItem
    # Model
admin.site.register(Manufacturer)
admin.site.register(CategoryItem)
admin.site.register(Model)
# Path: webscrapper/api/urls.py
# Compare this snippet from webscrapper/views.py:
