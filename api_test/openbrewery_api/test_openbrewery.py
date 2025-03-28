import pytest
from api_test.openbrewery_api import request, valid


def test_get_list_brewery(base_url):
    res = request.get_list_breweries(base_url)
    assert res.status_code == 200
    for brewery in res.json():
        assert valid.Brewery(**brewery)


@pytest.mark.parametrize('city', ['San Diego', 'Jangsu-gun', 'Sokcho-si'])
def test_get_brewery_with_filter_city(base_url, city):
    res = request.get_breweries_with_filter(base_url, flt='city', value=city)
    assert res.status_code == 200
    for brewery in res.json():
        assert valid.Brewery(**brewery)
        assert brewery['city'] == city


@pytest.mark.parametrize('size', [1, 50])
def test_get_random_brewery(base_url, size):
    res = request.get_random_brewery(base_url, value=size)
    assert res.status_code == 200
    for brewery in res.json():
        assert valid.Brewery(**brewery)
    assert len(res.json()) == size


@pytest.mark.parametrize('size', [0, 'y', True, False])
def test_get_invalid_random_brewery(base_url, size):
    res = request.get_random_brewery(base_url, value=size)
    assert len(res.json()) == 1


def test_get_max_size_list_random_brewery(base_url):
    res = request.get_random_brewery(base_url, value=51)
    assert len(res.json()) == 50


def test_meta_data(base_url):
    res = request.get_meta_data(base_url)
    assert res.status_code == 200
    assert valid.Metadata(**res.json())
