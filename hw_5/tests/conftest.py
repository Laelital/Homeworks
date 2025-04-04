import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome")
    parser.addoption(
        "--url",
        action="store",
        default="http://localhost:80")


@pytest.fixture(scope='module')
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
