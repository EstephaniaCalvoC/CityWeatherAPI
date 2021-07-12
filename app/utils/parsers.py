"""Define helpers functions to exract data weather object"""
from datetime import datetime
import uuid


def weather_parser(weather_resp):
    """Extract the weather data from the weather response"""

    cloudiness_lower = weather_resp.get("weather")[0].get("description")
    sunrise_utc = weather_resp.get("sys").get("sunrise")
    sunset_utc = weather_resp.get("sys").get("sunset")
    
    weather_dict = dict(
        code = str(uuid.uuid4()),
        temperature = weather_resp.get("main").get("temp"),
        wind_speed = weather_resp.get("wind").get("speed"),
        wind_deg = weather_resp.get("wind").get("deg"),
        cloudiness = cloudiness_lower.capitalize(),
        pressure = weather_resp.get("main").get("pressure"),
        humidity = weather_resp.get("main").get("humidity"),
        sunrise = datetime.fromtimestamp(sunrise_utc),
        sunset = datetime.fromtimestamp(sunset_utc),
    )

    return weather_dict


def forecast_parser(forecast_resp):
    """Extract the weather data from the weather response"""

    cloudiness_lower = forecast_resp.get("weather")[0].get("description")
    sunrise_utc = forecast_resp.get("sunrise")
    sunset_utc = forecast_resp.get("sunset")
    forecast_dict = dict(
        code = str(uuid.uuid4()),
        temperature = forecast_resp.get("temp").get("day"),
        wind_speed = forecast_resp.get("wind_speed"),
        wind_deg = forecast_resp.get("wind_deg"),
        cloudiness = cloudiness_lower.capitalize(),
        pressure = forecast_resp.get("pressure"),
        humidity = forecast_resp.get("humidity"),
        sunrise = datetime.fromtimestamp(sunrise_utc),
        sunset = datetime.fromtimestamp(sunset_utc)
    )

    return forecast_dict
