import pytest
import requests


@pytest.mark.parametrize('userId', [1, 5, 10])
def test_api_response(base_url, userId):
    res = requests.get(
        base_url + "/posts",
        params={'userId': userId}
    )
    assert res.status_code == 200


@pytest.mark.parametrize('id', [-1, 0, 101])
def test_api_empty_response(base_url, id):
    res = requests.get(
        base_url + "/posts",
        params={'id': id}
    )
    assert not res.json()





