
import requests

city = input("Enter city name: ")
url = "https://wttr.in/" + city + "?format=j1"

try:
    data = requests.get(url, timeout=10).json()
    print(data)
    weather = data["current_condition"][0]
    print("City:", city)
    print("Temperature:", weather["temp_C"], "°C")
    print("Humidity:", weather["humidity"], "%")
    print("Wind:", weather["windspeedKmph"], "km/h")
except Exception:
    print("Could not fetch the weather. ")