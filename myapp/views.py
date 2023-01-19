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


    return render(request, "home.html", context=data)
