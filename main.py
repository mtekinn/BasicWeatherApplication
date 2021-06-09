import requests
import json

location = input("Search city...")
end = "https://www.metaweather.com/api/location/search/?query={}".format(location)
response = requests.get(end)

# For filter cities
def cities_filter(response):
    cities = list(filter(lambda x: x.get('location_type') == "City", response))

    return cities


def cities_shown(cities):
    for id, city in enumerate(cities):
        print("Id: {}\nCity: {}".format(str(id), city.get("title")))


def forecast(woeid):
    forcastingEndpoint = "https://www.metaweather.com/api/location/{}/".format(woeid)
    response = requests.get(forcastingEndpoint)
    response_to_json = json.loads(response.content)
    consolidated_weather = response_to_json.get('consolidated_weather')
    for weather in consolidated_weather:
        print(weather.get("applicable_date"), weather.get("weather_state_name"))


if response.status_code == 200:
    cities_list = json.loads(response.content)
    cities = cities_filter(cities_list)
    cities_shown(cities)
    
    city_id = input("Please select the cities id: ")
    try:
        city_id = int(city_id)
        city = cities[city_id]
        city_woeid = city.get('woeid')
        forecast(city_woeid)
    except ValueError:
        print("Please enter a number!")