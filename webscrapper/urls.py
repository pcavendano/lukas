from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('device/<str:pk>', views.device, name='device'),
    path('scrappe/', views.scrappe, name='scrapper'),
    path('device_to_scrappe/', views.DeviceToScrappe, name='device_to_scrappe'),
]