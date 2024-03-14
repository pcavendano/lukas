from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('models/<str:pk>/', views.getModel, name='model_detail'),  # Renamed from 'models' to 'model_detail' for clarity
    path('models/', views.getModels, name='models'),
    path('devices/', views.getDevices, name='devices'),  # Renamed from 'models' to 'devices'
    path('updateManufacturers/', views.updateManufacturers, name='update_manufacturers'),  # Renamed for consistency
    path('scrapper/first-scrapper/', views.updateManufacturers),  # Consider removing this line if it's a duplicate
    path('manufacturers/', views.getManufacturers, name='manufacturers'),
    path('scrappe/<str:pk>/', views.getPrice, name='get_price'),  # Added trailing slash for consistency
    path('scrappe/', views.scrappe, name='scrappe'),
    path('scrappe/manufacturers/<str:pk>/', views.scrappeManufacturers, name='scrappe_manufacturer'),  # Added trailing slash for consistency
    path('iphonerepairprices/', views.getIphoneRepairPrices, name='iphone_repair_prices'),  # Added trailing slash for consistency
]