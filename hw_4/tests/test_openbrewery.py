import pytest
from hw_4.api_files.openbrewery_api import request_openbrewery as req, valid


@pytest.mark.base_url('https://api.openbrewerydb.org')
class TestOpenBrewery:
    """
    Набор тестов для проверки функциональности API
    на сайте https://www.openbrewerydb.org/
    """

    @pytest.mark.parametrize('num', [1, 100, 200])
    def test_get_list_breweries_valid_per_page(self, base_url, num):
        """ Граничные значения для запроса на вывод введенного количества пивоваренных заводов"""
        res = req.get_list_breweries_with_filter(base_url, 'per_page', num)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
        assert len(res.json()) == num

    @pytest.mark.parametrize('city', ['San Diego', 'Jangsu-gun', 'Sokcho-si'])
    def test_get_brewery_with_filter_city(self, base_url, city):
        """ Запрос на вывод списка пивоваренных заводов с фильтром city """
        res = req.get_list_breweries_with_filter(base_url, 'by_city', city)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
            assert brewery['city'] == city

    @pytest.mark.parametrize('by_name', ['san_diego', 'jangsu_gun', 'sokcho_si'])
    def test_get_brewery_with_filter_name(self, base_url, by_name):
        """ Запрос на вывод списка пивоваренных заводов с фильтром by_name """
        res = req.get_list_breweries_with_filter(base_url, 'by_name', by_name)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
            assert by_name.replace('_', ' ') in brewery['name'].lower()

    @pytest.mark.parametrize('size', [1, 50])
    def test_get_random_brewery(self, base_url, size):
        """ Граничные значения для запроса на вывод случайного пивоваренного завода """
        res = req.get_random_brewery(base_url, value=size)
        assert res.status_code == 200
        for brewery in res.json():
            assert valid.Brewery(**brewery)
        assert len(res.json()) == size

    @pytest.mark.parametrize('size', [0, 'y', True, False, 51])
    def test_get_invalid_random_brewery(self, base_url, size):
        """ Проверка дефолтного значения для запроса на вывод случайного пивоваренного завода """
        res = req.get_random_brewery(base_url, value=size)
        assert len(res.json()) == 1
