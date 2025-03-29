import pytest
from hw_4.api_files.openbrewery_api import request_openbrewery as req, valid


@pytest.mark.base_url('https://api.openbrewerydb.org')
class TestOpenBrewery:
    """
    Набор тестов для проверки функциональности API
    на сайте https://www.openbrewerydb.org/
    """

    def test_get_list_brewery(self, base_url):
        """ Запрос на вывод списка пивоваренных заводов"""
        res = req.get_list_breweries(base_url)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)

    @pytest.mark.parametrize('city', ['San Diego', 'Jangsu-gun', 'Sokcho-si'])
    def test_get_brewery_with_filter_city(self, base_url, city):
        """ Запрос на вывод списка пивоваренных заводов с фильтром city """
        res = req.get_breweries_with_filter(base_url, flt='city', value=city)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
            assert brewery['city'] == city

    @pytest.mark.parametrize('size', [1, 50])
    def test_get_random_brewery(self, base_url, size):
        """ Граничные значения для запроса на вывод случайного пивоваренного завода """
        res = req.get_random_brewery(base_url, value=size)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
        assert len(res.json()) == size

    @pytest.mark.parametrize('size', [0, 'y', True, False])
    def test_get_invalid_random_brewery(self, base_url, size):
        """ Проверка дефолтного значения для запроса на вывод случайного пивоваренного завода """
        res = req.get_random_brewery(base_url, value=size)
        assert len(res.json()) == 1

    def test_get_max_size_list_random_brewery(self, base_url):
        """ Проверка максимального значения для запроса на вывод случайного пивоваренного завода """
        res = req.get_random_brewery(base_url, value=51)
        assert len(res.json()) == 50

    def test_meta_data(self, base_url):
        """ Запрос на вывод метаданных """
        res = req.get_meta_data(base_url)
        assert res.status_code == 200
        assert valid.Metadata(**res.json())
