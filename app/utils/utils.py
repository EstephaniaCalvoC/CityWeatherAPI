from app.utils.conventions import wind_directions, wind_descriptions
from datetime import datetime

def convert_from_mps_to_kmph(mps):
    """Convert from mps (metters per second) to kmph (kilometters per hour)"""
    return 3.6 * mps


def get_hour_from_uts(date):
    """Return the date's hour and minute in a string like a digital clock"""
    hour = date.hour
    minute = date.minute
    return f"{hour:02}:{minute:02}"


def get_wind_direction(wind_deg):
    """Return the wind's direction description from wind degree"""
    for direction in wind_directions:
        if direction.get("min") <= wind_deg < direction.get("max"):
            
            return direction.get("direction")


def get_wind_descr(wind_speed):
    """Return the wind's description from wind speed"""
    wind_speed_kmh = convert_from_mps_to_kmph(wind_speed)
    for descr in wind_descriptions:
        if descr.get("min") <= wind_speed_kmh < descr.get("max"):
            return descr.get("descr")


def format_date(date):
    """Return a date with format %Y-%m-%d %H:%M:%S"""
    return date.strftime("%Y-%m-%d %H:%M:%S")
