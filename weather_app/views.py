from django.shortcuts import render
import requests

API_KEY = 'df540dfebb8b603f56331d22cf3b8931'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def index(request):
    return render(request, 'weather_app/index.html')

def get_weather(request):
    city = request.GET.get('city', '')  # Get the city from the query parameter
    if not city:
        error_message = "City not provided! Please enter a valid city name."
        return render(request, 'weather/index.html', {'error_message': error_message})
    
    # Debugging the API response
        print(f"API Response: {response.text}")  # This will log the response in the console


    # Make API call to OpenWeather to fetch weather data
    try:
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"  # units=metric for temperature in Celsius
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  # Parse the response JSON

            weather_data = {
                'city_name': data['name'],
                'temperature': data['main']['temp'],
                'weather_description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }

            return render(request, 'weather_app/index.html', weather_data)
        else:
            error_message = "City not found or API call failed. Please try again."
            return render(request, 'weather_app/index.html', {'error_message': error_message})

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching weather data: {str(e)}"
        return render(request, 'weather_app/index.html', {'error_message': error_message})
