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


def forcast_parser(forcast_resp):
    """Extract the weather data from the weather response"""

    cloudiness_lower = forcast_resp.get("weather")[0].get("description")
    sunrise_utc = forcast_resp.get("sunrise")
    sunset_utc = forcast_resp.get("sunset")
    forcast_dict = dict(
        code = str(uuid.uuid4()),
        temperature = forcast_resp.get("temp").get("day"),
        wind_speed = forcast_resp.get("wind_speed"),
        wind_deg = forcast_resp.get("wind_deg"),
        cloudiness = cloudiness_lower.capitalize(),
        pressure = forcast_resp.get("pressure"),
        humidity = forcast_resp.get("humidity"),
        sunrise = datetime.fromtimestamp(sunrise_utc),
        sunset = datetime.fromtimestamp(sunset_utc)
    )

    return forcast_dict
