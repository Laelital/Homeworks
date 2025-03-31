import requests


def list_all_breads(base_url):
    res = requests.get(f'{base_url}/breeds/list/all')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def random_image(base_url, num=''):
    res = requests.get(f'{base_url}/breeds/image/random/{num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def by_breed(base_url, breed):
    res = requests.get(f'{base_url}/breed/{breed}/images')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})
