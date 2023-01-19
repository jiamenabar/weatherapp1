from django.shortcuts import render

# Create your views here.

def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    xy = 1000
    data["time_of_day"] = time
    data['xy'] = xy
    city = request.GET.get('City')
    if city:
        temperature = WeatherApp.objects.get(city=city).temperature
        data['temperature'] = temperature
    else:
        data['temperature'] = None

    return render(request, "home.html", context=data)
