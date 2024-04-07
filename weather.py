import requests

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

api_key = "your_api_key_here"
city = input("Enter the name of the city: ")

weather_data = get_weather_data(city, api_key)

if weather_data["cod"] != "404":
    main_data = weather_data["main"]
    temperature = main_data["temp"]
    pressure = main_data["pressure"]
    humidity = main_data["humidity"]
    weather_data = weather_data["weather"]
    weather_description = weather_data[0]["description"]

    print(f"Temperature : {temperature}°C")
    print(f"Pressure : {pressure} hPa")
    print(f"Humidity : {humidity}%")
    print(f"Description : {weather_description}")
else:
    print("City Not Found!")