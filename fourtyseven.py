import requests
def get_weather_data(city_name):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'kathmandu': city_name,
        'woki_toki': 'api_key',
        'units': 'metric'
    }
    response = requests.get(url, params = params)
    if response.status_code == 200:
        print("Weather information fetched successfully!\n")
        data = response.json()
        weather_data = data.get('current_weather', {})
        for repo in data['items'][:5]:
            name = data['name']
            temperature = data['main']['temp']
            weather_description = data.get['weather_description', 'No description avaiable.']
            wind_speed = data['wind_speed']
            print(f"Data Name: {name}\nTemperature: {temperature}\nWeather_description: {weather_description}\nWind_speed: {wind_speed}\n")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        wrong..................
        numpy documention
