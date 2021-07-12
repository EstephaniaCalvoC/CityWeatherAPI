"""Test Weather Serializer class"""
from app.weather.weather import Weather
from app.weather.serializer import WeatherJsonEncoder
import json
from tests.test_weather.test_weather import gen_weather_data


def test_weather_json_econder():
    weather = Weather.from_dict(gen_weather_data())

    expected_json = f"""
        {{
            "temperature": "17 °C",
            "wind": "Gentle breeze, 3.6 m/s, southeast",
            "cloudiness": "Scattered clouds",
            "pressure": "1027 hpa",
            "humidity": "63%",
            "sunrise": "05:50",
            "sunset": "18:12"
        }}
    """

    json_weather = json.dumps(weather, cls=WeatherJsonEncoder)

    assert json.loads(json_weather) == json.loads(expected_json)
