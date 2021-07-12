"""Test City Serializer class"""
from app.city.city import City
from app.city.serializer import CityJsonEncoder
import json
from tests.test_city.test_city import gen_city_data


def test_city_json_econder():
    city = City.from_dict(gen_city_data())

    weather_text = """"temperature": "17 °C",
    "wind": "Gentle breeze, 3.6 m/s, southeast",
    "cloudiness": "Scattered clouds",
    "pressure": "1027 hpa",
    "humidity": "63%",
    "sunrise": "05:50",
    "sunset": "18:12","""

    forcast_text = weather_text[:-1]
    forcast_format = f"""{{{forcast_text}}}"""

    expected_json = f"""\
        {{
            "location": "Bogota, CO",
            {weather_text} 
            "geo_coordenates": "[4.6097, -74.0817]",
            "forcast": [
                {{"day1": {forcast_format}}},
                {{"day2": {forcast_format}}},
                {{"day3": {forcast_format}}},
                {{"day4": {forcast_format}}},
                {{"day5": {forcast_format}}},
                {{"day6": {forcast_format}}},
                {{"day7": {forcast_format}}}
            ],
            "requested_time": "2021-07-10 05:00:00"
        }}
    """

    json_city = json.dumps(city, cls=CityJsonEncoder)

    assert json.loads(json_city) == json.loads(expected_json)
