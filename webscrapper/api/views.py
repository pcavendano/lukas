from rest_framework.decorators import api_view
from rest_framework.response import Response
from webscrapper.models import Smarthphone
from webscrapper.models import Device
from .serializers import SmarthphoneSerializer
from .serializers import DeviceSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api',
            'method': 'GET',
            'body': None,
            'description': 'Returns this page'
        },
        {
            'Endpoint': '/api/devices',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of devices'
        },
        {
            'Endpoint': '/api/devices/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single device object by ID'
        },
        {
            'Endpoint': '/api/devices/create/',
            'method': 'POST',
            'body': 'Device object data in JSON format',
            'description': 'Creates a new device with data sent in the POST request'
        },
        {
            'Endpoint': '/api/devices/<int:id>/update/',
            'method': 'PUT',
            'body': 'Updated device object data in JSON format',
            'description': 'Updates a single device object by ID'
        },
        {
            'Endpoint': '/api/devices/<int:id>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a single device object by ID'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getDevices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDevice(request, pk):
    device = Device.objects.get(id=pk)
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSmarthphone(srequest):
    smarthphones = Smarthphone.objects.all()
    serializer = SmarthphoneSerializer(smarthphones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSmarthphone(request, pk):
    smarthphone = Smarthphone.objects.get(id=pk)
    serializer = SmarthphoneSerializer(smarthphone, many=False)
    return Response(serializer.data)