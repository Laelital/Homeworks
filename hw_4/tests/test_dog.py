import pytest
from hw_4.api_files.dog_api.valid import BreedsList, BreedsImage
from hw_4.api_files.dog_api.request_dog_api import list_all_breads, random_image, by_breed


@pytest.mark.base_url('https://dog.ceo/api')
class TestDogApi:
    """
    Набор тестов для проверки функциональности API
    на сайте https://dog.ceo/api
    """

    def test_list_all_breeds(self, base_url):
        """ Запрос на вывод всех пород """
        res = list_all_breads(base_url)
        assert res.status_code == 200
        assert BreedsList(**res.json())
        assert res.json()['status'] == 'success'

    def test_random_image(self, base_url):
        """ Случайная фотография собаки """
        res = random_image(base_url)
        assert res.status_code == 200
        assert BreedsImage(**res.json())
        assert res.json()['status'] == 'success'

    @pytest.mark.parametrize('num', [1, 50])
    def test_list_random_image_valid_borders(self, base_url, num):
        """ Граничные значения для случайных фотографий животных"""
        res = random_image(base_url, num)
        assert res.status_code == 200
        assert BreedsImage(**res.json())
        assert len(res.json()['message']) == num  # количество фотографий совпадает с введенным числом

    @pytest.mark.parametrize('breed', ['papillon', 'pomeranian', 'dalmatian', 'collie'])
    def test_by_valid_breed(self, base_url, breed):
        """ Проверка поиска по породе """
        res = by_breed(base_url, breed)
        assert res.status_code == 200
        assert BreedsImage(**res.json())
        assert res.json()['status'] == 'success'

    @pytest.mark.parametrize('breed', ['папийон', 'померанский', 'далматинец', 'колли'],
                             ids=['papillon', 'pomeranian', 'dalmatian', 'collie'])
    def test_by_invalid_breed(self, base_url, breed):
        """ Проверка поиска по породе на кириллице """
        res = by_breed(base_url, breed)
        assert res.status_code == 404
