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

    choice = request.GET.get('City')
    data['city_choice']=choice

    if choice:
        weather_bar = WeatherApp.objects.filter(city=choice)
        data['temperature'] = WeatherApp.objects.filter(city=choice).values('weather')
        data['city'] = WeatherApp.objects.filter(city=choice).values('city')
    else:
        data['temperature'] = None
        data['country'] = None

    return render(request, "home.html", context=data)
