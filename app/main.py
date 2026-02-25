import os
import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")

    if not API_KEY:
        raise Exception("Please set your environment variable `API_KEY`")

    URL = "http://api.weatherapi.com/v1/current.json"

    CITY = "Paris"
    PARAMS = {
        "key": API_KEY,
        "q": CITY,
    }

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params=PARAMS)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
