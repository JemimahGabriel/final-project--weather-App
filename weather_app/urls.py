from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This is for the main page of the weather app
    path('get_weather/', views.get_weather, name='get_weather'),  # Add the URL for 'get_weather'
]
