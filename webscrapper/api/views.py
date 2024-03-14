from rest_framework.decorators import api_view
from rest_framework.response import Response
from webscrapper.models import Model
from .serializers import ModelsSerializer
from .serializers import ManufacturerSerializer
from webscrapper.models import ModelPrice
from webscrapper.models import RepairPrices  # Add this import

import requests
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse

from webscrapper.models import Manufacturer
from webscrapper.models import CategoryItem
from webscrapper.models import Model
from django.db.models import OuterRef, Subquery
from django.http import JsonResponse
from requests_html import HTMLSession
import re
from bs4 import BeautifulSoup




@api_view(['GET'])
def getDevices(request):
    def get_devices_with_last_price():
        latest_price_subquery = ModelPrice.objects.filter(
            model=OuterRef('pk')
        ).order_by('-created').values('price')[:1]

        devices_with_last_price = Model.objects.annotate(
            last_price=Subquery(latest_price_subquery)
        )
        return devices_with_last_price

    devices_with_last_price = get_devices_with_last_price()
    serializer = ModelsSerializer(devices_with_last_price, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api',
            'method': 'GET',
            'body': None,
            'description': 'Retourne cette page'
        },
        {
            'Endpoint': '/api/models',
            'method': 'GET',
            'body': None,
            'description': 'Retourne un tableau de modèles'
        },
        {
            'Endpoint': '/api/models/:id',
            'method': 'GET',
            'body': None,
            'description': 'Retourne un seul objet de modèle par ID'
        },
        {
            'Endpoint': '/api/models/<int:id>/update/',
            'method': 'PUT',
            'body': 'Données mises à jour de l\'objet de modèle au format JSON',
            'description': 'Met à jour un seul objet de modèle par ID'
        },
        {
            'Endpoint': '/api/models/<int:id>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Supprime un seul objet de modèle par ID'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getModels(request):
    models = Model.objects.all()
    paginator = Paginator(models, 10)  # Show 10 models per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = ModelsSerializer(page_obj, many=True)  # Serialize the paginated queryset
    
    data = serializer.data  # Use serialized data instead of manually converting QuerySet to list of dictionaries
    
    return JsonResponse({'data': data, 'page': page_obj.number, 'total_pages': paginator.num_pages})

@api_view(['GET'])
def getModel(request, pk):
    model = Model.objects.get(model_id=int(pk))
    serializer = ModelsSerializer(model, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getManufacturers(request):
    manufacturer = Manufacturer.objects.all()
    serializer = ManufacturerSerializer(manufacturer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def scrappe(request):
    url = "https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code=AP&cache=true"
    try:
        # Envoyer une requête GET à l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi (code de statut 200)
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
                model_name_without_memorygb = re.sub(r'\d+GB', '', model_name_without_manufacturer).strip()                
                # Replace spaces with hyphens
                model_name_without_memorygb = model_name_without_memorygb.replace(' ', '-')
                # Convert to lowercase
                model_name_without_memorygb = model_name_without_memorygb.lower()
                img = getImagesFromUrlWithBeutifulSoup(manufacturer.manufacturer_name.lower(), model_name_without_memorygb)
                print("Image URL: ")
                print(img)
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
                        model_title=model_name_without_memorygb,
                        category_item=category_item,
                        image=img
                        
                    )
                    print(f"Le modèle avec l'ID {model_data['model_id']} a été créé avec succès.")

        else:
            print(f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}")
            return {"error": f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}"}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {"error": f"Une erreur s'est produite : {e}"}
    #script_path = 'webscrapper/scrappers/bell_scrapper.py'
    #subprocess.run(['python', script_path])
    print("Script de scrapping exécuté avec succès!")
    return HttpResponse("Script de scrapping exécuté avec succès.")

@api_view(['GET'])
def getPrice(request, pk):
    # Assuming `pk` is the product code needed for scraping
    scrape_url = "https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/getBuyBackProductsEstimate?session_id=893351c7-d359-4462-a9fd-1ea5cce4343c&buyer_code=REDEEM&product_code=" + pk
    buyback_price = ModelPrice.scrape_and_save(scrape_url, pk)
    print(f'Buyback price for product code {pk}: {buyback_price}')
    
    return JsonResponse({'buyback_price': buyback_price})

@api_view(['GET'])
def scrappeManufacturers(request, pk):
    url = "https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code="+pk+"&cache=true"
    try:
        # Envoyer une requête GET à l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi (code de statut 200)
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
                model_name_without_memorygb = re.sub(r'\d+GB', '', model_name_without_manufacturer).strip()                
                # Replace spaces with hyphens
                model_name_without_memorygb = model_name_without_memorygb.replace(' ', '-')
                # Convert to lowercase
                model_name_without_memorygb = model_name_without_memorygb.lower()
                img = getImagesFromUrlWithBeutifulSoup(manufacturer.manufacturer_name.lower(), model_name_without_memorygb)
                print("Image URL: ")
                print(img)
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
                        model_title=model_name_without_memorygb,
                        category_item=category_item,
                        image=img
                        
                    )
                    print(f"Le modèle avec l'ID {model_data['model_id']} a été créé avec succès.")

        else:
            print(f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}")
            return {"error": f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}"}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {"error": f"Une erreur s'est produite : {e}"}
    #script_path = 'webscrapper/scrappers/bell_scrapper.py'
    #subprocess.run(['python', script_path])
    print("Script de scrapping exécuté avec succès!")
    return HttpResponse(" exécuté avec succès.")

def getImagesFromUrlWithBeutifulSoup(manufacturer, url):
    imageUrl = 'https://www.gizmochina.com/product/' + manufacturer+"-" + url
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    response = requests.get(imageUrl, headers=headers)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find the img tag
        img_tag = soup.find('img', class_='aps-image-zoom')
        if img_tag:
            # Extract the src attribute
            src = img_tag.get('src')
            if src:
                print(src)
            else:
                print("Image src attribute not found.")
        else:
            print("Image not found on the page.")
    else:
        print(f"An error occurred: {response.status_code}")
        print(f"An error occurred: {imageUrl}")
        return "https://www.gizmochina.com/wp-content/uploads/2024/03/1-500x500.jpg"
    if src:
        return src

@api_view(['GET'])
def updateManufacturers(request):
    # Create an HTMLSession object
    session = HTMLSession()
    # # Make a GET request to a URL
    response = session.get( "https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/getManufacturers?session_id=1b254d76-565d-416e-b36a-9551d1e3b9f1&view_parameters=TRADEIN")
    try:
        # Envoyer une requête GET à l'URL
        response = session.get( "https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/getManufacturers?session_id=1b254d76-565d-416e-b36a-9551d1e3b9f1&view_parameters=TRADEIN")

        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Convertir le contenu de la réponse en JSON
            json_data = response.json()
            for model_data in json_data['manufacturers']:
                if model_data is not None and 'parameters' in model_data and model_data['parameters'] is not None:
                    if len(model_data['parameters']) > 0 and 'param_value' in model_data['parameters'][0]:
                        active = model_data['parameters'][0]['param_value']
                        if active == "1":
                            # Your code here
                            manufacturer_id = model_data['manufacturer_id']
                            # Enregistrer le fabricant
                            manufacturer, _ = Manufacturer.objects.get_or_create(
                                manufacturer_id=model_data['manufacturer_id'],
                                manufacturer_code=model_data['manufacturer_code'],
                                manufacturer_name=model_data['manufacturer_name']
                            )
                            print(f"Le modèle avec l'ID {model_data['manufacturer_id']} a été créé avec succès.")

                            # Enregistrer le modèle uniquement si le mode_id n'existe pas
                            existing_model = Manufacturer.objects.filter(manufacturer_id=model_data['manufacturer_id']).first()
                            if existing_model:
                                print(f"Le manufacturer avec l'ID {model_data['manufacturer_id']} existe déjà.")
                            else:
                                # Enregistrer le modèle
                                Manufacturer.objects.create(
                                    manufacturer_id=model_data['manufacturer_id'],
                                    manufacturer_code=model_data['manufacturer_code'],
                                    manufacturer_name=model_data['manufacturer_name'],
                                )
                                print(f"Le modèle avec l'ID {model_data['model_id']} a été créé avec succès.")
                        else:
                            print(f"Le manufacturer {model_data['manufacturer_name']} est désactivé.")
                    else:
                        print("No 'param_value' found in the first parameter.")
                else:
                    print("model_data or model_data['parameters'] is None.")
        else:
            print(f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}")
            return {"error": f"Échec de la récupération de l'URL : {url}. Code de statut : {response.status_code}"}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {"error": f"Une erreur s'est produite : {e}"}
    #script_path = 'webscrapper/scrappers/bell_scrapper.py'
    #subprocess.run(['python', script_path])
    print("Script de scrapping exécuté avec succès!")
    return HttpResponse("Script de scrapping exécuté avec succès.")

@api_view(['GET'])
def getIphoneRepairPrices(request):
    repairUrl = "https://mobileklinik.ca/repair-pricing-breakdown/#apple"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    
    response = requests.get(repairUrl, headers=headers)
    try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                table = soup.find('table', class_='table table-striped repair-price-table apple')
                rows = table.find_all('tr')
                for row in rows[2:]:  # Skip header row
                    print("Row: ")
                    print(row)
                    cols = row.find_all('td')
                    print("Cols: ")
                    print(cols)
                    device_name = cols[0].text.strip("<sup class='smaller-sup'>†</sup>")
                    print("device_name")
                    print(device_name)
                    screen_repair_price_mk = re.sub(r'<[^>]+>', '', cols[1].text.strip()).replace('$', '')
                    # remove everything after the space even the space
                    screen_repair_price_mk = re.sub(r'\s.*', '', screen_repair_price_mk)
                    
                    if screen_repair_price_mk == "–":
                        screen_repair_price_mk = 0
                    print("screen_repair_price_mk")
                    print(screen_repair_price_mk)
                    
                    screen_repair_price_apple = re.sub(r'<[^>]+>', '', cols[2].text.strip()).replace('$', '')
                    #remove everything after the space even the space
                    screen_repair_price_apple = re.sub(r'\s.*', '', screen_repair_price_apple)
                    if screen_repair_price_apple == "–":
                        screen_repair_price_apple = 0
                    print("screen_repair_price_apple")
                    print(screen_repair_price_apple)
                    
                    battery_repair_price_mk = re.sub(r'<[^>]+>', '', cols[3].text.strip()).replace('$', '')
                    #remove everything after the space even the space
                    battery_repair_price_mk = re.sub(r'\s.*', '', battery_repair_price_mk)
                    if battery_repair_price_mk == "–":
                        battery_repair_price_mk = 0
                    print("battery_repair_price_mk")
                    print(battery_repair_price_mk)
                    
                    battery_repair_price_apple = re.sub(r'<[^>]+>', '', cols[4].text.strip()).replace('$', '')
                    #remove everything after the space even the space
                    battery_repair_price_apple = re.sub(r'\s.*', '', battery_repair_price_apple)
                    if battery_repair_price_apple == "–":
                        battery_repair_price_apple = 0
                    print("battery_repair_price_apple")
                    print(battery_repair_price_apple)
                    
                    charge_port_repair_price_mk = re.sub(r'<[^>]+>', '', cols[5].text.strip()).replace('$', '')
                    #remove everything after the space even the space
                    charge_port_repair_price_mk = re.sub(r'\s.*', '', charge_port_repair_price_mk)
                    if charge_port_repair_price_mk == "–":
                        charge_port_repair_price_mk = 0
                    print("charge_port_repair_price_mk")
                    print(charge_port_repair_price_mk)
                    name_lower_case = device_name.lower()
                    name_lower_case = name_lower_case.replace(' ', '-')
                    print("name_lower_case")
                    print(name_lower_case)
                    existing_model = Model.objects.filter(model_title = name_lower_case).first()
                    print("existing_model")
                    print(existing_model)
                    if existing_model:
                        RepairPrices.objects.create(
                        model=existing_model,
                        device_name=device_name,
                        screen_repair_price_mk=float(screen_repair_price_mk),
                        screen_repair_price_apple=float(screen_repair_price_apple),
                        battery_repair_price_mk=float(battery_repair_price_mk),
                        battery_repair_price_apple=float(battery_repair_price_apple),
                        charge_port_repair_price_mk=float(charge_port_repair_price_mk)
                        )
                        print(f"La réparation des prix pour le modèle {device_name} a été créée avec succès.")
                    else:
                        print(f"Model not found for device: {device_name}")
                return True
            else:
                print(f"Failed to fetch URL: {repairUrl}. Status Code: {response.status_code}")
                return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
        
                