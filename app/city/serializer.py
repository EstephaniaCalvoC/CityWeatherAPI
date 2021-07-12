"""Define a serializer class to encode the city object to JSON"""
from app.utils.utils import format_date
from app.weather.serializer import get_weather_dict_to_serilize
from datetime import datetime
import json


def get_city_dict_to_serilizer(city):
    """Return a dictionary to serilize a City object"""
    current_weather = get_weather_dict_to_serilize(city.current_weather)
    latitude = city.geo_coordenates.get("lat")
    longitude = city.geo_coordenates.get("lon")
    daily_forecast = [{f"day{n + 1}": get_weather_dict_to_serilize(forecast)}
        for n, forecast in enumerate(city.daily_forecast)]
    requested_time = format_date(city.requested_time)

    to_serilize = {"location": city.location}
    to_serilize.update(current_weather)
    to_serilize.update({"geo_coordenates": f"[{latitude}, {longitude}]"})
    to_serilize.update({"forecast": daily_forecast})
    to_serilize.update({"requested_time": requested_time})

    return to_serilize


class CityJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serilize = get_city_dict_to_serilizer(obj)
            return to_serilize
        except AttributeError:
            return super().default(obj)
