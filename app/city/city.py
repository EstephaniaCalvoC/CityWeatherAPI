"""Define the City Class"""
from app.weather.weather import Weather
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class City():
    """
    Class to define a city object
    """

    code: str
    location: str
    current_weather: Weather
    geo_coordenates: dict
    daily_forcast: list
    requested_time: datetime

    @classmethod
    def from_dict(self, data):
        return City(**data)

    def to_dict(self):
        return dataclasses.asdict(self)
