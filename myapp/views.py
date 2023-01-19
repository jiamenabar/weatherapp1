from django.shortcuts import render
from myapp.models import WeatherApp
import requests
from .models import City
from .forms import CityForm
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
        weather_bar = WeatherApp.objects.get(city=choice)
        data['temperature'] = weather_bar.weather
    else:
        data['temperature'] = None

    return render(request, "home.html", context=data)

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c6653f6c9abb06e0a3dd17d64a2e8145'

    cities = City.objects.all()  # return all the cities in the database

    form = CityForm()

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data}

    return render(request, 'index.html', context)  # returns the index.html template