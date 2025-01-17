import requests

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
city = 'Kathmandu'
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Make a GET request to fetch weather data
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    print(f"The temperature in {city} is {temperature}°C.")
else:
    print("Failed to fetch weather data")

    # wrong
