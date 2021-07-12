"""Test API city weather"""

import pytest
import api as weather_api
import time


@pytest.fixture
def client():
    weather_api.app.config['TESTING'] = True

    with weather_api.app.test_client() as client:
        yield client

def test_get_city_weather():
    with weather_api.app.test_client() as client:
        time.sleep(120)
        resp = client.get('/weather?city=tokyo&country=JP')

        assert resp.status == "200 OK"

def test_bad_request():
    with weather_api.app.test_client() as client:
        time.sleep(120)
        resp = client.get('/weather?city=tokyo&country=CO')

        assert resp.status != "200 OK"

def test_cache():
    with weather_api.app.test_client() as client:
        time.sleep(120)
        resp1 = client.get('/weather?city=cali&country=CO')
        time.sleep(60)
        resp2 = client.get('/weather?city=bogota&country=CO')
        time.sleep(60)
        resp3 = client.get('/weather?city=medellin&country=CO')

        assert resp1.data == resp2.data
        assert resp2.data != resp3.data
