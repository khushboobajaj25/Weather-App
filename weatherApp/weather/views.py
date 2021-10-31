from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.views import View
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
class WeatherView(View):
    def get(self,request,city=None):
        print(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=36c304bc5f045c421f2d468b5c7ed422&units=metric"
        data = requests.get(url).json()
        if data.get("message")!=None:
            return JsonResponse(data)
        city_weather={
            "city":city,
            "temperature":data["main"]["temp"],
            "description":data["weather"][0]["description"],
            "icon":data["weather"][0]["icon"],
            "pressure":  data["main"]["pressure"],
            "longitude":data["coord"]["lon"],
            "latitude":data["coord"]["lat"],
            "humidity":data["main"]["humidity"],
            "countryCode":data["cod"],
            "foreCast":data["weather"][0]["main"]
        }
        return JsonResponse(city_weather)
