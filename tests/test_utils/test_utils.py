"""Test helper functions"""
from app.utils.conventions import wind_directions, wind_descriptions
from app.utils.utils import wind_directions, wind_descriptions,\
    convert_from_mps_to_kmph, get_hour_from_uts, get_wind_direction,\
    get_wind_descr
from tests.test_weather.test_weather import gen_weather_data


def test_convert_from_mps_to_kmph():
    actual = convert_from_mps_to_kmph(100)
    expected = 360

    assert actual == expected


def test_get_hour_from_uts():
    weather_data = gen_weather_data()
    actual = get_hour_from_uts(weather_data.get("sunrise"))
    expected = "05:50"

    assert actual == expected


def test_get_wind_direction_min_degree():
    for segment in wind_directions:
        wind_deg = segment.get("min")
        actual = get_wind_direction(wind_deg)
        expected = segment.get("direction")
        assert actual == expected


def test_get_wind_direction_max_degree():
    for segment in wind_directions:
        wind_deg = segment.get("max")
        actual = get_wind_direction(wind_deg)
        expected = segment.get("direction")

        assert actual != expected


def  test_get_wind_direction():
    for segment in wind_directions:
        wind_deg = (segment.get("min") + segment.get("max")) / 2
        actual = get_wind_direction(wind_deg)
        expected = segment.get("direction")

        assert actual == expected

def test_def_get_wind_descr_min_speed():
    for segment in wind_descriptions:
        wind_speed = segment.get("min") / 3.6
        actual = get_wind_descr(wind_speed)
        expected = segment.get("descr")

        assert actual == expected


def test_def_get_wind_descr_max_speed():
    for segment in wind_descriptions:
        wind_speed = segment.get("max") / 3.59
        actual = get_wind_descr(wind_speed)
        expected = segment.get("descr")

        assert actual != expected


def test_def_get_wind_descr():
    for segment in wind_descriptions:
        wind_speed = (segment.get("min") + segment.get("max")) / (2 * 3.6)
        actual = get_wind_descr(wind_speed)
        expected = segment.get("descr")

        assert actual == expected
