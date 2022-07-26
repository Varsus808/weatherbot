import requests
import pathlib

path_to_openweather_cred =str(pathlib.Path().resolve())+'/openweather_credentials.txt'

with open(path_to_openweather_cred, 'r') as f:
    for line in f:
        if line[-1] == '\n':
            openweather_api_key = line[:-1]
        else:
            openweather_api_key = line

def weather_warrior(city='london'):
	api_call=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric&lang=de'
	data = requests.get(api_call).json()
	print(data)
	return data['main']['temp'], data['weather'][0]['description']


