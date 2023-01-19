from django.db import models

# Create your models here.
class WeatherApp(models.Model):
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    weather = models.FloatField(default=0.0)
    def __str__(self):
        return self.city + " " + self.country + " " + str(self.weather)
    def __repr__(self):
        return self.city + " " + self.country + " " + str(self.weather)
