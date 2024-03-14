import os
import django
import requests
from webscrapper.models import Manufacturer
from webscrapper.models import CategoryItem
from webscrapper.models import Model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def scrape_and_save(url):
    # Fonction pour extraire les données d'un site web et renvoyer la réponse JSON
    try:
        # Envoyer une requête GET à l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi (code de statut 200)
        print(response)
        if response.status_code == 200:
            # Convertir le contenu de la réponse en JSON
            json_data = response.json()
            for model_data in json_data['models']:
                manufacturer_data = model_data['manufacturer']
                category_item_data = model_data['category_item']

                # Enregistrer le fabricant
                manufacturer, _ = Manufacturer.objects.get_or_create(
                    manufacturer_id=manufacturer_data['manufacturer_id'],
                    manufacturer_code=manufacturer_data['manufacturer_code'],
                    manufacturer_name=manufacturer_data['manufacturer_name']
                )

                # Enregistrer l'élément de catégorie
                category_item, _ = CategoryItem.objects.get_or_create(
                    item_id=category_item_data['item_id'],
                    item_order=category_item_data['item_order'],
                    item_name=category_item_data['item_name']
                )

                model_name_without_manufacturer = model_data['model_name'].replace(manufacturer.manufacturer_name, '').strip()
                # Enregistrer le modèle uniquement si le mode_id n'existe pas
                existing_model = Model.objects.filter(model_id=model_data['model_id']).first()
                if existing_model:
                    print(f"Le modèle avec l'ID {model_data['model_id']} existe déjà.")
                else:
                    # Enregistrer le modèle
                    model = Model.objects.create(
                        manufacturer=manufacturer,
                        model_id=model_data['model_id'],
                        model_code=model_data['model_code'],
                        model_name=model_name_without_manufacturer,
                        model_title=model_data['model_title'],
                        category_item=category_item
                    )
                    print(f"Le modèle avec l'ID {model_data['model_id']} a été créé avec succès.")

        else:
            print(f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}")
            return {"error": f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}"}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {"error": f"Une erreur s'est produite : {e}"}

# Exemple d'utilisation
if __name__ == "__main__":
    # Remplacez 'example.com/api/data' par l'URL qui renvoie du JSON
    scrape_and_save("https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code=AP&cache=true")
