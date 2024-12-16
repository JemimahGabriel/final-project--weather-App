from django.contrib import admin
from django.urls import path, include  # Include to include app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin dashboard
    path('', include('weather_app.urls')),  # Direct to the weather_app's URLs
]
