import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default='https://dog.ceo/api',
        help="This is request url"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
