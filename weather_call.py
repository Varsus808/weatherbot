import requests

API='426ccf0f0247a6612b299246fb671c5F'

with open('/home/micha/weatherbot/openweather_credentials.txt', 'r') as f:
    for line in f:
        if line[-1] == '\n':
            openweather_api_key = line[:-1]
        else:
            openweather_api_key = line

def weather_warrior(City='krefeld'):
	api_call=f'https://api.openweathermap.org/data/2.5/weather?q={City}&appid={openweather_api_key}&units=metric&lang=de'
	data = requests.get(api_call).json()
	print(data)
	return data['main']['temp'], data['weather'][0]['description']


