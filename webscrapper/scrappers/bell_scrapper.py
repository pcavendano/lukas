import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
import requests
import json
from webscrapper.models import Manufacturer
from webscrapper.models import Model
from webscrapper.models import CategoryItem

def scrape_and_save(url):
    # Function to scrape a website and return the JSON response
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response content to JSON
            json_data = response.json()
            print(json_data)
            for model_data in json_data['models']:
                manufacturer_data = model_data['manufacturer']
                category_item_data = model_data['category_item']

                # Save Manufacturer
                manufacturer, _ = Manufacturer.objects.get_or_create(
                    manufacturer_id=manufacturer_data['manufacturer_id'],
                    manufacturer_code=manufacturer_data['manufacturer_code'],
                    manufacturer_name=manufacturer_data['manufacturer_name']
                )

                # Save CategoryItem
                category_item, _ = CategoryItem.objects.get_or_create(
                    item_id=category_item_data['item_id'],
                    item_order=category_item_data['item_order'],
                    item_name=category_item_data['item_name']
                )

                # Save Model
                model, created = Model.objects.get_or_create(
                    manufacturer=manufacturer,
                    model_id=model_data['model_id'],
                    model_code=model_data['model_code'],
                    model_name=model_data['model_name'],
                    model_title=model_data['model_title'],
                    category_item=category_item
                )
                
                # Optionally print a message indicating whether the model was created or not
                if created:
                    print(f"Model {model.model_name} created successfully.")
                else:
                    print(f"Model {model.model_name} already exists.")

        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return {"error": f"Failed to fetch URL: {url}. Status code: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": f"An error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    # Replace 'example.com/api/data' with the URL that returns JSON
    scrape_and_save("https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code=AP&cache=true")
