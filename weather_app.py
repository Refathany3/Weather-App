
import requests

# API key from OpenWeatherMap (use your own API key here)
api_key = "your_api_key"

# Base URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# City input from the user
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Get weather data
response = requests.get(complete_url)
data = response.json()

# Check if city is found
if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_desc = data["weather"][0]["description"]
    
    # Print the weather information
    print(f"Temperature: {temperature} K")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_desc}")
else:
    print("City not found!")
