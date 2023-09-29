from weather_api import get_weather_forecast

def get_weather_info(user):
    weather_code = user['daily']['time'][0]['weathercode']
    max_temp = user['daily']['time'][0]['temperature_2m_max']
    min_temp = user['daily']['time'][0]['temperature_2m_min']

    return weather_code, max_temp, min_temp

def get_weather_description(weather_code):
    descriptions = {
        1: "Clear sky",
        2: "Nearly clear sky",
        3: "Variable cloudiness",
        # Add more descriptions as needed
    }

    return descriptions.get(weather_code, "Unknown weather code")

def main():
    user = get_weather_forecast()
    weather_code, max_temp, min_temp = get_weather_info(user)
    description = get_weather_description(weather_code)

    print(f"Weather Forecast for Today:")
    print(f"Description: {description}")
    print(f"Max Temperature: {max_temp}°C")
    print(f"Min Temperature: {min_temp}°C")

if __name__ == "__main__":
    main()
