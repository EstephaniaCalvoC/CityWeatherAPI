# City Weather API 🌞

REST API to get weather information from a city

## Requirements
- Python 3.8
- Ubuntu 20

## How to run
1. Set APIKEY variable 
    ```bash
    echo -e '\nOPEN_WEATHER_API_KEY="{your_key}"' >> ~/.bashrc
    sudo source ~/.bashrc
    ```

    **Note:** You must get your key in [Open Weather API](https://openweathermap.org/api)

2. Install requirements 
    ```bash
    pip install -r requirements.txt
    ```

3. Run the API 
    ```bash
    python api.py
    ```

4. Request something
    ```bash
    curl -X GET "http://127.0.0.1:5000/weather?city=tokyo&country=JP"
    ```
    **Note:** You also can try with [Postman](https://www.postman.com/)

5. Testing
* Run all test except the API test
    ```bash
    pytest -svv --ignore=tests/test_api.py
    ```
* Run only API test
    ```bash
    pytest tests.test_api.py
    ```
    **Note:** The test take eight minutes arround, because the api test wait two minutes to clean the cache and make a request.

* Run all test
    ```bash
    pytest -svv
    ```

---

## Output Example
```json
{
    "location": "Bogota, CO",
    "temperature": "13.73 °C",
    "wind": "Light breeze, 2.57 m/s, east",
    "cloudiness": "Broken clouds",
    "pressure": "1028 hpa",
    "humidity": "77%",
    "sunrise": "05:50",
    "sunset": "18:12",
    "geo_coordenates": "[4.6097, -74.0817]",
    "forcast": [
        {
            "day1": {
                "temperature": "16.5 °C",
                "wind": "Light breeze, 1.87 m/s, south-southeast",
                "cloudiness": "Light rain",
                "pressure": "1016 hpa",
                "humidity": "70%",
                "sunrise": "05:50",
                "sunset": "18:12"
            }
        },
        {
            "day2": {
                "temperature": "14.02 °C",
                "wind": "Light breeze, 2.15 m/s, south-southeast",
                "cloudiness": "Light rain",
                "pressure": "1018 hpa",
                "humidity": "81%",
                "sunrise": "05:50",
                "sunset": "18:12"
            }
        },
        {
            "day3": {
                "temperature": "16.64 °C",
                "wind": "Light breeze, 1.78 m/s, east-southeast",
                "cloudiness": "Light rain",
                "pressure": "1017 hpa",
                "humidity": "65%",
                "sunrise": "05:50",
                "sunset": "18:12"
            }
        },
        {
            "day4": {
                "temperature": "12.62 °C",
                "wind": "Light breeze, 1.71 m/s, southeast",
                "cloudiness": "Light rain",
                "pressure": "1019 hpa",
                "humidity": "85%",
                "sunrise": "05:51",
                "sunset": "18:12"
            }
        },
        {
            "day5": {
                "temperature": "17.01 °C",
                "wind": "Light breeze, 1.7 m/s, south-southeast",
                "cloudiness": "Light rain",
                "pressure": "1015 hpa",
                "humidity": "66%",
                "sunrise": "05:51",
                "sunset": "18:12"
            }
        },
        {
            "day6": {
                "temperature": "16.58 °C",
                "wind": "Light breeze, 1.82 m/s, southeast",
                "cloudiness": "Light rain",
                "pressure": "1015 hpa",
                "humidity": "68%",
                "sunrise": "05:51",
                "sunset": "18:12"
            }
        },
        {
            "day7": {
                "temperature": "13.26 °C",
                "wind": "None, 1.6 m/s, east-southeast",
                "cloudiness": "Light rain",
                "pressure": "1017 hpa",
                "humidity": "87%",
                "sunrise": "05:51",
                "sunset": "18:13"
            }
        },
        {
            "day8": {
                "temperature": "13.19 °C",
                "wind": "Light breeze, 1.84 m/s, east-southeast",
                "cloudiness": "Light rain",
                "pressure": "1018 hpa",
                "humidity": "83%",
                "sunrise": "05:51",
                "sunset": "18:13"
            }
        }
    ],
    "requested_time": "2021-07-12 04:36:17"
}
```
---

### Author

* **Estephania Calvo Carvajal** - [LinkedIn](https://www.linkedin.com/in/estephaniacalvoc/)
