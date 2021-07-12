from app.city.repository import ApiRepo
from app.city.use_case import city_weather_info_use_case
from app.city.serializer import CityJsonEncoder
from app.city.response.response_type import ResponseTypes
from app.request.CityWeatherInfoValReq import build_city_weather_info_request

from flask import Flask, request, Response
from flask_app.config import cache_config
from flask_caching import Cache
import json

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

cache = Cache(config=cache_config)
app = Flask(__name__)
cache.init_app(app)
timeout = cache_config.get("CACHE_DEFAULT_TIMEOUT")


@app.route("/weather", methods=["GET"])
@cache.memoize(timeout)
def get_city_weather():
    """Handle GET requests"""
    city = request.args.get("city")
    country = request.args.get("country")

    qrystr_params = {"city": city, "country": country}

    request_object = build_city_weather_info_request(params=qrystr_params)

    repo = ApiRepo()
    response = city_weather_info_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=CityJsonEncoder, ensure_ascii=False),
        mimetype="application/json",
        status=STATUS_CODES[response.type],
    )


if __name__ == "__main__":
    app.run(debug=True)
