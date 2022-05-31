import requests
import keyboard
while True:
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = input('City Name :')
    url = api_address + city + "&units=metric"
    json_data = requests.get(url).json()
    weather = json_data['weather'][0]['description']
    print("The weather is " + weather)
    Temp = json_data['main']['temp']
    print("Temperature of " + city + " " + str(Temp)+ "°")
    Humidity = json_data['main']['humidity']
    print("Humidity of " + city + " " + str(Humidity))
    Wind = json_data['wind']['speed']
    print("Speed of wind in " + city + " " + str(Wind))

    print("----------------------------------------------------")
    print("Do you want to continue? (y/n)")
    if keyboard.read_key() == "n":
        break
