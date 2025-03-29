import requests
import pytest


@pytest.fixture(scope='module')
def status_code(request):
    return request.config.getoption('--status_code')


def test_status_code(base_url, status_code):
    assert requests.get(base_url).status_code == int(status_code)
