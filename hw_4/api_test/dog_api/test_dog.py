import pytest
from api_test.dog_api.valid import BreedsList, BreedsImage
from api_test.dog_api.request import list_all_breads, random_image, by_breed


def test_list_all_breeds(base_url):
    res = list_all_breads(base_url)
    assert res.status_code == 200                # статус код 200
    assert BreedsList(**res.json())              # валидация полей
    assert res.json()['status'] == 'success'     # статус "успешный"


def test_random_image(base_url):
    res = random_image(base_url)
    assert res.status_code == 200                # статус код 200
    assert BreedsImage(**res.json())             # валидация полей
    assert res.json()['status'] == 'success'     # статус "успешный"


@pytest.mark.parametrize('num', [1, 50])         # проверка граничных значений
def test_list_random_image_valid_borders(base_url, num):
    res = random_image(base_url, num)
    assert res.status_code == 200                # статус код 200
    assert BreedsImage(**res.json())             # валидация полей
    assert len(res.json()['message']) == num     # количество картинок совпадает с введенным числом


@pytest.mark.parametrize('breed', ['papillon', 'pomeranian', 'dalmatian', 'collie'])
def test_by_breed(base_url, breed):              # проверка поиска по породе
    res = by_breed(base_url, breed)
    assert res.status_code == 200                # статус код 200
    assert BreedsImage(**res.json())             # валидация полей
    assert res.json()['status'] == 'success'     # статус "успешный"


@pytest.mark.parametrize('breed', ['папийон', 'померанский', 'далматинец', 'колли'],
                         ids=['papillon', 'pomeranian', 'dalmatian', 'collie'])
def test_by_invalid_breed(base_url, breed):      # проверка на кириллицу
    res = by_breed(base_url, breed)
    assert res.status_code == 404                # статус код 404
