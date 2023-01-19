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

    weather_list = WeatherApp.objects.all()
    data['weather_list'] = weather_list

    city = request.GET.get('City')
    if city:
        city, country = city.split()
        temperature = WeatherApp.objects.get(city=city, country=country).weather
        data['temperature'] = temperature
    else:
        data['temperature'] = None

    return render(request, "home.html", context=data)
