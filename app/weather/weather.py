"""Define the Weather Class"""
import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Weather():
    """
    Class to define a weather object
    """

    code: str
    temperature: int
    wind_speed: float
    wind_deg: float
    cloudiness: str
    pressure: float
    humidity: float
    sunrise: datetime
    sunset: datetime

    @classmethod
    def from_dict(self, data):
        return Weather(**data)


    def to_dict(self):
        return dataclasses.asdict(self)
