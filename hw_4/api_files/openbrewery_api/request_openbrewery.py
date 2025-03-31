import requests


def get_list_breweries_with_filter(base_url, flt='', num=1):
    res = requests.get(f'{base_url}/v1/breweries?{flt}={num}')
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
