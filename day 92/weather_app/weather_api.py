import requests

def get_weather_forecast():
    timezone = "GMT"
    latitude = 51.5002
    longitude = -0.1262

    result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

    user = result.json()
    return user
