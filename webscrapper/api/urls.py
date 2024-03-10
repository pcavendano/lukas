from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('devices/', views.getDevices, name='devices'),
    path('devices/<str:pk>/', views.getDevice),
]