import requests


def get_single_brewery(base_url, obdb_id):
    res = requests.get(f'{base_url}/v1/breweries/{obdb_id}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_list_breweries(base_url):
    res = requests.get(f'{base_url}/v1/breweries')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_breweries_with_filter(base_url, flt, value):
    res = requests.get(f'{base_url}/v1/breweries?by_{flt}={value}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_random_brewery(base_url, value=1):
    res = requests.get(f'{base_url}/v1/breweries/random?size={value}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_meta_data(base_url):
    res = requests.get(f'{base_url}/v1/breweries/meta')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})