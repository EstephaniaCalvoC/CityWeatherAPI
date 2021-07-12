"""Testing the Weather class"""
from app.weather.weather import Weather
from datetime import datetime
import uuid


def gen_weather_data():
    code = str(uuid.uuid4())
    sunrise = datetime.fromtimestamp(1625914223)
    sunset = datetime.fromtimestamp(1625958759)
    init_dict = {
        "code": code,
        "temperature": 17,
        "wind_speed": 3.6,
        "wind_deg": 137,
        "cloudiness": "Scattered clouds",
        "pressure": 1027,
        "humidity": 63,
        "sunrise": sunrise,
        "sunset": sunset
    }
    return init_dict


def test_weather_model_init():
    init_dict = gen_weather_data()

    weather = Weather(**init_dict)

    assert weather.code == init_dict.get("code")
    assert weather.temperature == 17
    assert weather.wind_speed == 3.6
    assert weather.wind_deg == 137
    assert weather.cloudiness == "Scattered clouds"
    assert weather.pressure == 1027
    assert weather.humidity == 63
    assert weather.sunrise == init_dict.get("sunrise")
    assert weather.sunset == init_dict.get("sunset")


def test_weather_from_dict():
    init_dict = gen_weather_data()

    weather = Weather.from_dict(init_dict)

    assert weather.code == init_dict.get("code")
    assert weather.temperature == 17.0
    assert weather.wind_speed == 3.6
    assert weather.wind_deg == 137
    assert weather.cloudiness == "Scattered clouds"
    assert weather.pressure == 1027
    assert weather.humidity == 63
    assert weather.sunrise == init_dict.get("sunrise")
    assert weather.sunset == init_dict.get("sunset")


def test_weather_to_dict():
    init_dict = gen_weather_data()

    weather = Weather(**init_dict)
    assert weather.to_dict() == init_dict
