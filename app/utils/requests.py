"""Define helpers functions to make request to Open Weather API"""
from flask_app.config import open_weather_config
import json
import requests


def req_current_weather(city, country):
    """\
    Return the response of the request to Open Weather API
    to get the current weather
    """

    headers = {'content-type': 'application/json'}
    url = open_weather_config.get("CURRENT_URL").format(
        api_key=open_weather_config.get("API_KEY"),
        city=city,
        country=country
    )

    response = requests.get(url=url, headers=headers)

    response_dict = (json.loads(response.text))

    return response_dict


def req_daily_forecast(lat, lon):
    """\
    Return the response of the request to Open Weather API
    to get the daily forecast
    """

    headers = {'content-type': 'application/json'}
    url = open_weather_config.get("ONE_CALL_URL").format(
        api_key=open_weather_config.get("API_KEY"),
        lat=lat,
        lon=lon,
        part=open_weather_config.get("EXCLUSIONS")
    )
    response = requests.get(url=url, headers=headers)

    response_dict = (json.loads(response.text))

    return response_dict
