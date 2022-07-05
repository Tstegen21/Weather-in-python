#Importing relevant libraries
import requests
from datetime import datetime
import weather_cred
#generating a request and strog
url = 'https://api.openweathermap.org/data/2.5/weather?'
CITY = input('Enter a city of which the weather you want to know:')
API_KEY= weather_cred.credentials
full_api = url +'appid='+ API_KEY +'&q='+ CITY
response = requests.get(full_api).json()
temperature = response['main']['temp']
feels_like = response['main']['feels_like']
humidity = response['main']['humidity']
wind = response['wind']['speed']
sunrise = datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset = datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

def temp_convert(kelvin):
    celsius = kelvin-273.15
    fahren =  celsius*1.8 -32
    return celsius,fahren

temperature_c,temperature_f = temp_convert(temperature)
feels_likec,feels_likef = temp_convert(feels_like)

print(f'The Temperature for the city of {CITY} is : {temperature_c:.2f}°C')
print(f'But It actually feels like {feels_likec:.2f}°C ')
print(f'The time for sunrise in the {CITY} is:{sunrise.time().replace(microsecond=0)}. ')
print(f'And the time for sunset in the {CITY} is:{sunset.time().replace(microsecond=0)}. ')


