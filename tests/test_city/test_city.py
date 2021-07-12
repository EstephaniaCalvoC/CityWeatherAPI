"""Testing the City class"""
from app.city.city import City
from app.weather.weather import Weather
from datetime import datetime
from tests.test_weather.test_weather import gen_weather_data
import uuid


def gen_city_data():
    code = str(uuid.uuid4())
    current_weather = Weather.from_dict(gen_weather_data())
    daily_forcast = [Weather.from_dict(gen_weather_data()) for i in range(7)]

    init_dict = {
        "code": code,
        "location": "Bogota, CO",
        "current_weather": current_weather,
        "daily_forcast": daily_forcast,
        "geo_coordenates": {"lat": 4.6097, "lon": -74.0817},
        "requested_time": datetime(2021, 7, 10, 5, 0, 0)
    }

    return init_dict


def test_city_init():
    init_dict = gen_city_data()
    city = City(**init_dict)

    assert city.code == init_dict.get("code")
    assert city.location == "Bogota, CO"
    assert city.current_weather == init_dict.get("current_weather")
    assert city.daily_forcast == init_dict.get("daily_forcast")
    assert city.geo_coordenates == {"lat": 4.6097, "lon": -74.0817}
    assert city.requested_time == init_dict.get("requested_time")

def test_city_from_dict():
    init_dict = gen_city_data()
    city = City.from_dict(init_dict)

    assert city.code == init_dict.get("code")
    assert city.location == "Bogota, CO"
    assert city.current_weather == init_dict.get("current_weather")
    assert city.daily_forcast == init_dict.get("daily_forcast")
    assert city.geo_coordenates == {"lat": 4.6097, "lon": -74.0817}
    assert city.requested_time == init_dict.get("requested_time")

def test_city_to_dict():
    init_dict = gen_city_data()
    daily_forcast = init_dict.get("daily_forcast")
    
    city = City.from_dict(init_dict)
    init_dict["current_weather"] = init_dict.get("current_weather").to_dict()
    dict_daily_forcast = [forcast.to_dict() for forcast in daily_forcast]
    init_dict["daily_forcast"] = dict_daily_forcast

    assert city.to_dict() == init_dict
