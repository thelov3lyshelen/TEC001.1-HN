import requests
import time
import json
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])

time.sleep(1)

api = "774fe325b648e54f06f5f02ef2aacaa1"
city = input("Enter city name: ")

geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api}"
georesponse = requests.get(geo).json()
try:
    lat = georesponse[0]["lat"]
    lon = georesponse[0]["lon"]
    print("Getting coordiantes...")
    time.sleep(1)
    print(f"Lattitude: {lat}, Longtitude: {lon}")
except:
    print("City not found!")
weather = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api}&units=metric"
weatherresponse = requests.get(weather)
print(weatherresponse)
if weatherresponse.status_code == 401:
    print("Service broken, redirecting to OpenWeather 2.5....")
    time.sleep(1)
    weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    weatherresponse = requests.get(weather).json()
    temperature = weatherresponse["main"]["temp"] - 273.15
    weatherdata = weatherresponse["weather"][0]["description"]
    print(f"{city}: {weatherdata}, {temperature} degrees Celsius")
elif weatherresponse.status_code != 200:
    print("Invalid response")
else:
    output = weatherresponse.json()
    weatherdata = output["current"]["weather"][0]["description"]

    temperature = weatherdata["temp"]
    print(f"{city}: {weatherdata},{temp} degrees Celsius")
# too bad i dont have a credit card