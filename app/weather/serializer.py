"""Define a serializer class to encode the weather object to JSON"""
import json
from app.utils.utils import get_hour_from_uts, get_wind_descr, get_wind_direction

def get_weather_dict_to_serilize(weather):
    """Return a dictionary to serilize a Weather object"""
    wind_desc = get_wind_descr(weather.wind_speed)
    wind_direction = get_wind_direction(weather.wind_deg)
    sunrise_hour = get_hour_from_uts(weather.sunrise)
    sunset_hour = get_hour_from_uts(weather.sunset)
    to_serilize = {
        "temperature": f"{weather.temperature} \u00b0C",
        "wind": f"{wind_desc}, {weather.wind_speed} m/s, {wind_direction}",
        "cloudiness": weather.cloudiness,
        "pressure": f"{weather.pressure} hpa",
        "humidity": f"{weather.humidity}%",
        "sunrise": f"{sunrise_hour}",
        "sunset": f"{sunset_hour}"
    }
    return to_serilize

class WeatherJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serilize = get_weather_dict_to_serilize(obj)
            print(to_serilize)
            return to_serilize
        except AttributeError:
            return super().default(obj)
