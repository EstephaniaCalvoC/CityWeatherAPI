"""Define City Weather Info Valid Request class"""
from app.request.CityWeatherInfoInvReq import CityWeatherInfoInvReq


class CityWeatherInfoValReq:
    def __init__(self, params=None):
        self.params = params

    def __bool__(self):
        return True


def build_city_weather_info_request(params=None):
    invalid_req = CityWeatherInfoInvReq()

    if params is not None:
        city = params.get("city")
        country = params.get("country")

        if not isinstance(city, str):
            invalid_req.add_error("city", "Must be a string")

        if not isinstance(country, str):
            invalid_req.add_error("country", "Must be a string")
        elif (len(country) != 2):
            invalid_req.add_error("country", "Must have two letters")

        if invalid_req.has_errors():
            return invalid_req

    return CityWeatherInfoValReq(params=params)
