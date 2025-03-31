import random
import pytest
from hw_4.api_files.jsonplace import valid, request_jsonplaceholder as req


@pytest.mark.base_url('https://jsonplaceholder.typicode.com')
class TestJsonPlaceHolder:
    """
    Набор тестов для проверки функциональности API
    на сайте https://jsonplaceholder.typicode.com/
    """

    @pytest.mark.parametrize('num', [1, 100])
    def test_get_post(self, base_url, num):
        """ Граничные значения для запроса постов"""
        res = req.get_resource(base_url, 'posts', num)
        assert res.status_code == 200
        assert valid.Post(**res.json())

    @pytest.mark.parametrize('num', [1, 10])
    def test_get_user(self, base_url, num):
        """ Граничные значения для запроса пользователей"""
        res = req.get_resource(base_url, 'users', num)
        assert res.status_code == 200
        assert valid.User(**res.json())

    @pytest.mark.parametrize('num', [1, 100])
    def test_get_comment_with_filter(self, base_url, num):
        """ Граничные значения для запроса комментариев с фильтром postId"""
        res = req.get_resource_with_filter(base_url, 'comments', 'postId', num)
        assert res.status_code == 200
        for comment in res.json():
            assert valid.Comment(**comment)

    @pytest.mark.parametrize('num', [1, 200])
    def test_get_list_todos_with_filter(self, base_url, num):
        """ Граничные значения для запроса задач с фильтром id"""
        res = req.get_resource_with_filter(base_url, 'todos', 'id', num)
        assert res.status_code == 200
        for todos in res.json():
            assert valid.Todos(**todos)

    def test_post_new_post(self, base_url, input_title='title', input_body='body', input_id=1):
        """ Создание нового поста с валидными данными"""
        res = req.post_new_post(base_url, input_title='title', input_body='body', input_id=1)
        assert valid.Post(**res)
        assert res['title'] == input_title
        assert res['body'] == input_body
        assert res['userId'] == str(input_id)
