import math
math.sqrt(25)

from math import sqrt, pi
sqrt(25)
pi

import random
random.randint(1, 100)
random.choice(["manzana", "plátano", "naranja"])

import datetime 
datetime.date.today()

import os 
os.getcwd()

import json
data = {"name": "Juan Gabriel", "age": 37}
json.dumps(data)

import pandas as pd
import numpy as np

import datetime as dt 
dt.date.today()

from math import * 
sin(2*pi)

import requests 

response = requests.get("https://api.example.com/data")
data = response.json()

import pandas as pd
data = {
    'name': ["Juan Gabriel", "Alicia", "Mario"],
    'age': [37, 30, 25],
    'city': ["Palma de Mallorca", "Nueva York", "Londres"]
}

df = pd.DataFrame(data)
print(df)

import requests 

latitude = 39.593
longitude = 2.680 

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()
print(data)

temperature = data['current']['temperature_2m']
print(f"La temperatura en Palma de Mallorca es {temperature}ºC")

import requests

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    temperature = data['current']['temperature_2m']
    return temperature

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}ºC")
print(f"Londres: {london_temp}ºC")
print(f"Tokyo: {tokyo_temp}ºC")


import requests
from datetime import datetime, timedelta

today = datetime.now()
week_ago = today - timedelta(days = 7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

start_date
end_date

latitude = 39.593
longitude = 2.680 

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

import pandas as pd

daily_data = data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})
df['date'] = pd.to_datetime(df['date'])
print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['date'], df['max_temp'], marker='o', label="Max Temp")
plt.plot(df['date'], df['min_temp'], marker='o', label="Min Temp")

plt.xlabel('Fecha')
plt.ylabel('Temperatura (ºC)')
plt.title("Temperatura de Palma de Mallorca - Últimos 7 días")
plt.legend()

plt.xticks(rotation = 45)
plt.tight_layout()

plt.savefig("weather_chart.png")
plt.show()

import os

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/palma_weather.csv', index=False)
print('Los datos se han guardado correctamente en la carpeta data!')