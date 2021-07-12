import os

API_KEY = os.environ.get("OPEN_WEATHER_API_KEY") or "c1847c3158c474bf8ceef6e14630b613"
cache_config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 120
}

open_weather_config = {
    "API_KEY": API_KEY,
    "ONE_CALL_URL": "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}&units=metric",
    "CURRENT_URL": "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric",
    "EXCLUSIONS": "minutely,hourly,alerts"
}
