from django.contrib import admin
from myapp.models import WeatherApp
from .models import City

# Register your models here.

class WeatherAdmin(admin.ModelAdmin):
    fields = ('city','country','weather')

admin.site.register(WeatherApp,WeatherAdmin)

from django.contrib.auth.models import User

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

admin.site.register(City)