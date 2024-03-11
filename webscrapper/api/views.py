from rest_framework.decorators import api_view
from rest_framework.response import Response
from webscrapper.models import Model
from .serializers import ModelsSerializer
import subprocess
from django.http import HttpResponse

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
    serializer = ModelsSerializer(models, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getModel(request, pk):
    model = Model.objects.get(id=pk)
    serializer = ModelsSerializer(model, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def scrappe(request):
    # Supposons que vous ayez un sérialiseur défini pour vos données de réponse
    # serializer = VotreSérialiseur(data)
    
    # Définissez le chemin vers le script scrapper.py
    script_path = 'webscrapper/scrappers/bell_scrapper.py'

    # Exécutez le script à l'aide de subprocess
    subprocess.run(['python', script_path])

    # Ajoutez toute logique supplémentaire pour votre fonction de vue
    # ...
    print("Script de scrapping exécuté avec succès.")
    return HttpResponse("Script de scrapping exécuté avec succès.")
