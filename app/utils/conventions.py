"""Declare the winter descriptions conventions"""


wind_directions = (
    {"min": 348.75, "max": 361, "direction": "north"},
    {"min": 0, "max": 11.25, "direction": "north"},
    {"min": 11.25, "max": 33.75, "direction": "north-northeast"},
    {"min": 33.75, "max": 56.25, "direction": "northeast"},
    {"min": 56.25, "max": 78.75, "direction": "east-northeast"},
    {"min": 78.75, "max": 101.25, "direction": "east"},
    {"min": 101.25, "max": 123.75, "direction": "east-southeast"},
    {"min": 123.75, "max": 146.25, "direction": "southeast"},
    {"min": 146.25, "max": 168.75, "direction": "south-southeast"},
    {"min": 168.75, "max": 191.25, "direction": "south"},
    {"min": 191.25, "max": 213.75, "direction": "south-southwest"},
    {"min": 213.75, "max": 236.25, "direction": "southwest"},
    {"min": 236.25, "max": 258.75, "direction": "west-southwest"},
    {"min": 258.75, "max": 281.25, "direction": "west"},
    {"min": 281.25, "max": 303.75, "direction": "west-northwest"},
    {"min": 303.75, "max": 326.25, "direction": "northwest"},
    {"min": 326.25, "max": 348.75, "direction": "north-northwest"}
)

wind_descriptions = (
    {"min": 0, "max": 1, "descr": "Calm"},
    {"min": 1, "max": 5, "descr": "Light air"},
    {"min": 6, "max": 11, "descr": "Light breeze"},
    {"min": 12, "max": 19, "descr": "Gentle breeze"},
    {"min": 20, "max": 28, "descr": "Moderate breeze"},
    {"min": 29, "max": 38, "descr": "Fresh breeze"},
    {"min": 39, "max": 49, "descr": "Strong breeze"},
    {"min": 50, "max": 61, "descr": "Near gale"},
    {"min": 62, "max": 74, "descr": "Gale"},
    {"min": 75, "max": 88, "descr": "Strong gale"},
    {"min": 89, "max": 102, "descr": "Storm"},
    {"min": 103, "max": 117, "descr": "Violent storm"},
    {"min": 118, "max": 500, "descr": "Hurricane"},
)
