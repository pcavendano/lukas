from rest_framework.serializers import ModelSerializer
from webscrapper.models import Smarthphone
from webscrapper.models import Device




class SmarthphoneSerializer(ModelSerializer):
    class Meta:
        model = Smarthphone
        fields = '__all__'

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'