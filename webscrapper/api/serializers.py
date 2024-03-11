from rest_framework.serializers import ModelSerializer
from webscrapper.models import Model, Manufacturer

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class ModelsSerializer(ModelSerializer):
    manufacturer = ManufacturerSerializer()  # Include the nested manufacturer field
    class Meta:
        model = Model
        fields = '__all__'

