import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def lookup(name):
    configure()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name.upper()}&appid={os.getenv("api_key")}&units=metric"

    print(os.getenv("api_key"))

    try:
        response = requests.get(url)
        response.raise_for_status()
        contents = response.json()

        return {
            "description": contents["weather"][0]["description"].capitalize(),
            "temperature": contents["main"]["temp"],
            "feels_like": contents["main"]["feels_like"],
            "wind": contents["wind"]["speed"],
            "humidity": contents["main"]["humidity"],
            "country": contents["sys"]["country"],
            "name": name.upper()
        }
    
    except requests.HTTPError:
        print("Couldn't complete request.")
        return