from django.shortcuts import render
from myapp.models import WeatherApp
# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    xy = 1000
    data["time_of_day"] = time
    data['xy'] = xy

    cities = WeatherApp.objects.values_list('city', flat=True).distinct()
    data['cities'] = cities

    city = request.GET.get('city')
    if city:
        temperature = WeatherApp.objects.get(city=city).weather
        data['temperature'] = temperature
    else:
        data['temperature'] = None

    return render(request, "home.html", context=data)
