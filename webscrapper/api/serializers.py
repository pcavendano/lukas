from rest_framework import serializers
from .models import getDevice




class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = getDevice
        fields = '__all__'