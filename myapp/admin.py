from django.contrib import admin
from myapp.models import WeatherApp

# Register your models here.

class WeatherAdmin(admin.ModelAdmin):
    fields = ('city','country','weather')
    model = WeatherApp
    extra = 0

admin.site.register(WeatherApp,WeatherAdmin)