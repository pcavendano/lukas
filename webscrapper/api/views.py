from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import getDevice
from .serializers import DeviceSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/devices',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of devices'
        },
        {
            'Endpoint': '/api/devices/<int:id>',
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
    devices = getDevice.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)