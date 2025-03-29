import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        default='https://ya.ru'
    )

    parser.addoption(
        "--status_code",
        default=200
    )


@pytest.fixture
def base_url(request):
    marker = request.node.get_closest_marker('base_url')
    if marker:
        return marker.args[0]
    else:
        return request.config.getoption("--base_url")
