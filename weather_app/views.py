

# Create your views here.
import requests
from django.shortcuts import render

API_KEY = '1e38b36a2c67bd4195e29f2a9c11ed0c'

def dashboard(request):
    city = request.GET.get('city', 'London')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json() if response.status_code == 200 else None

    context = {
        'data': data,
        'city': city,
    }
    return render(request, 'weather_app/dashboard.html', context)
