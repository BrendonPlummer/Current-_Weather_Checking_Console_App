import requests
import os
import json
from datetime import datetime

user_api = os.environ.get('FETCH_WEATHER_API_KEY')
location = input("Please input location to search: ")

FETCH_COORDS_API_LINK = "http://api.openweathermap.org/geo/1.0/direct?q="+ location +"&limit=5&appid=" + user_api

locationFetch = requests.get(FETCH_COORDS_API_LINK)
locationCoords = locationFetch.json()
# print(locationCoords)
lat = locationCoords[0]['lat']
lon = locationCoords[0]['lon']

COMPLETE_API_LINK = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + user_api

api_link = requests.get(COMPLETE_API_LINK).json()
#print(api_link)

if(api_link['cod'] == '404'):
    print("Invalid City: {}, please check city name.".format(location))
else:
    temperature = (api_link['main']['temp']) - 273.15
    weather_desc = api_link['weather'][0]['description']
    humidty = api_link['main']['humidity']
    wind_speed = api_link['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    
    print("----------------------------------------------------------------------")
    print("Weather Statistics for - {} || {}".format(location.upper(), date_time))
    print("----------------------------------------------------------------------")
    
    print("Current temperature is: {:.2f}C.".format(temperature))
    print("Weather for today is: {}.".format(weather_desc))
    print("Humidity for today is: {}.".format(humidty))
    print("Wind speed today is approx.: {}mph.".format(wind_speed))
    
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")