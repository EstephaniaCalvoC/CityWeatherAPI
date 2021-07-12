"""Define repository class"""
from app.city.city import City
from app.weather.weather import Weather
from app.utils.parsers import weather_parser, forcast_parser
from app.utils.requests import req_current_weather, req_daily_forcast
from datetime import datetime
import uuid


class ApiRepo:

    def get_city_weather_info(self, params):
        """Get the current weather info"""
        req_city = params.get("city")
        req_country = params.get("country")

        weather_resp = req_current_weather(req_city, req_country)
        lat = weather_resp.get("coord").get("lat")
        lon = weather_resp.get("coord").get("lon")

        forcast_resps = req_daily_forcast(lat, lon)
        daily = forcast_resps.get("daily")

        name = weather_resp.get("name")
        country_code = weather_resp.get("sys").get("country").upper()
        location = f"{name}, {country_code}"

        forcast_dicts = [forcast_parser(forcast) for forcast in daily]
        daily_forcast = [Weather.from_dict(forcast_dict)
            for forcast_dict in forcast_dicts]

        weather_dict = weather_parser(weather_resp)

        city_dict = dict(
            code = str(uuid.uuid4()),
            location = location,
            current_weather = Weather.from_dict(weather_dict),
            geo_coordenates = {"lat":lat, "lon":lon},
            daily_forcast = daily_forcast,
            requested_time = datetime.utcnow()
        )

        city = City.from_dict(city_dict)

        return city
