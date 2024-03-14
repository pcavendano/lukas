import os
import django
import requests
import sys
from webscrapper.models import Model


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def scrape_and_save(url):
    print("aqui")
    print(url)
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            buyback_value = json_data["products"][0]["buyback_values"][0]["value"]
            model_code = json_data["products"][0]["product_code"]

            existing_model = Model.objects.filter(model_code=model_code).first()
            if existing_model:
                # Update the existing model with the new buyback value
                existing_model.buyback_value_max = buyback_value
                existing_model.save()
                print(f"Model with ID {model_code} updated successfully with buyback value: {buyback_value}")
            else:
                print(f"Model with ID {model_code} does not exist.")

        else:
            print(f"Failed to fetch URL: {url}. Status Code: {response.status_code}")
            return {"error": f"Failed to fetch URL: {url}. Status Code: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": f"An error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    pk = "TI9443"
    # Replace 'example.com/api/data' with the URL that returns JSON
    scrape_and_save("https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/getBuyBackProductsEstimate?session_id=893351c7-d359-4462-a9fd-1ea5cce4343c&buyer_code=REDEEM&product_code="+ pk)
