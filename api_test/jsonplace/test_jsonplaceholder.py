import random
import pytest
import requests

from api_test.jsonplace import valid, request


@pytest.mark.parametrize('num', [1, 100])
def test_get_post(base_url, num):
    res = request.get_post(base_url, num)
    assert res.status_code == 200
    assert valid.Post(**res.json())


@pytest.mark.parametrize('num', [1, 10])
def test_get_user(base_url, num):
    res = request.get_user(base_url, num)
    assert res.status_code == 200
    assert valid.User(**res.json())


@pytest.mark.parametrize('flt', ['postId', 'id'])
def test_get_comment_with_filter(base_url, flt):
    if flt == 'id':
        num = random.randint(1, 500)
    else:
        num = random.randint(1, 100)
    res = request.get_comments_with_filter(base_url, flt, num)
    assert res.status_code == 200
    for comment in res.json():
        assert valid.Comment(**comment)


@pytest.mark.parametrize('flt', ['userId', 'id', 'completed'])
def test_get_list_todos_with_filter(base_url, flt):
    if flt == 'id':
        num = random.randint(1, 200)
    elif flt == 'completed':
        num = bool(random.randint(0, 1))
    else:
        num = random.randint(1, 10)
    res = request.get_list_todos_with_filter(base_url, flt, num)
    assert res.status_code == 200
    for todos in res.json():
        assert valid.Todos(**todos)


def test_post_new_post(base_url, input_title='title', input_body='body', input_id=1):
    res = requests.post(
        base_url + '/posts',
        data={'title': input_title, 'body': input_body, 'userId': input_id}
    ).json()
    assert valid.Post(**res)
    assert res['title'] == input_title
    assert res['body'] == input_body
    assert res['userId'] == str(input_id)


