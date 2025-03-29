import requests


def get_post(base_url, num=''):
    res = requests.get(f'{base_url}/posts/{num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_user(base_url, num=''):
    res = requests.get(f'{base_url}/users/{num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_comments_with_filter(base_url, flt='id', num=1):
    res = requests.get(f'{base_url}/comments?{flt}={num}')
    try:
        return res
    except requests.exceptions.RequestException:
        print('Ошибка, статус код: ', {res.status_code})


def get_list_todos_with_filter(base_url, flt='id', num=1):
    res = requests.get(f'{base_url}/todos?{flt}={num}')
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
