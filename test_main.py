from main import get_temperature
import pytest
import requests

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {'currently':{'temperature': 62}}

@pytest.mark.parametrize("lat, lng, expect", [(-14.235004, -51.92528, 16)])
def test_get_temperature_by_lat_lng(monkeypatch, lat, lng, expect):
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(lat, lng)

    assert result == expect

# https://docs.pytest.org/en/latest/monkeypatch.html