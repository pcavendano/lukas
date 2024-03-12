from django.db import models
import requests


# Create your models here.
# This is where we configure our database schema
class WebsitesToScrappe(models.Model):
    url = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
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
    

class ModelPrice(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='prices')
    id = models.AutoField(primary_key=True)
    model_code = models.CharField(max_length=20, default='')
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']  # Orders by date added, newest first

    
    @staticmethod
    def scrape_and_save(url, pk):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                model_code = json_data["products"][0]["product_code"]
                buyback_value = json_data["products"][0]["buyback_value_max"]
                print(model_code)
                print('aca')
                existing_model = Model.objects.filter(model_code=model_code).first()
                print(existing_model)
                model = ModelPrice.objects.create(
                    model_code=model_code,
                    model=existing_model,
                    price=buyback_value
                )
                print(f"Le modèle avec l'ID {model} a été créé avec succès.")

            else:
                print(f"Failed to fetch URL: {url}. Status Code: {response.status_code}")
                return {"error": f"Failed to fetch URL: {url}. Status Code: {response.status_code}"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": f"An error occurred: {e}"}