"""Define city_weather_info_use_case function"""

from app.city.response.response_success import ResponseSuccess
from app.city.response.response_failure import ResponseFailure,\
    build_response_from_invalid_request
from app.city.response.response_type import ResponseTypes


def city_weather_info_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        city_weather_info = repo.get_city_weather_info(request.params)
        return ResponseSuccess(city_weather_info)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
