import requests
import sys

def get_weather(city, api_key):
    payload={'q' : city, 'appid': api_key}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', payload)
    weather_data = {}
    data = r.json()
    try:
        weather_data['Temperature'] = data['main']['temp']
        weather_data['Condition'] = data['weather'][0]['description']
        weather_data['Humidity'] = data['main']['humidity']
        weather_data['Wind Speed'] = data['wind']['speed'] 

        display_weather(city, weather_data)
    except:
        print('Some error has occured', data['message'])

def display_weather(city, weather_data):
    print("\nWeather in ", city)
    print("\nTemperature: ", weather_data['Temperature'])
    print("Condition: ", weather_data['Condition'])
    print("Humidity: ", weather_data['Humidity'])
    print("Wind Speed: ", weather_data['Wind Speed'], end="\n")
    
    return

def main():
    API_KEY = 'e9f6767df1367e8fc62a46820733b2df'
    print("\nWeather report application")
    print("1. Get weather information")
    print("2. Exit", end="\n")
    val = int(input("\nEnter your choice: "))

    if(val == 1):
        city = input("Enter your city name: ")
        get_weather(city, API_KEY)
    else:
        sys.exit()
    
    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    main()
