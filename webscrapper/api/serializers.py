from rest_framework import serializers
from webscrapper.models import Model, Manufacturer, ModelPrice, RepairPrices

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class ModelPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPrice
        fields = ('price', 'created')  # Assuming you want to include price and creation date only

class ModelsSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    last_price = serializers.SerializerMethodField()

    def get_last_price(self, obj):
        last_price_instance = obj.prices.order_by('-created').first()
        if last_price_instance:
            return last_price_instance.price
        return None

    class Meta:
        model = Model
        fields = '__all__'

class RepairPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairPrices
        fields = '__all__'
