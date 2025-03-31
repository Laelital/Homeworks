import requests


def get_resource(base_url, resource='', num=''):
    res = requests.get(f'{base_url}/{resource}/{num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_resource_with_filter(base_url, resource='', flt='', num=1):
    res = requests.get(f'{base_url}/{resource}?{flt}={num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def post_new_post(base_url, input_id, input_title, input_body):
    res = requests.post(f'{base_url}/posts',
                        data={'title': input_title,
                              'body': input_body,
                              'userId': input_id})
    res_json = res.json()
    return res_json
