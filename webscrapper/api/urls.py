from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('scrappe/', views.scrappe, name='scrappe'),
    path('models/', views.getModels, name='models'),
    path('models/<str:pk>/', views.getModel),
]