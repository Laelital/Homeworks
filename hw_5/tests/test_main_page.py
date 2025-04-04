from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:
    def test_check_navbar(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".navbar-nav")))
        navbar_list = browser.find_elements(By.CSS_SELECTOR, ".navbar-nav")
        for category in navbar_list:
            category.get_attribute("href")

    def test_check_navbar_dropdown(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".navbar-nav")))
        navbar_list = browser.find_elements(By.CSS_SELECTOR, ".navbar-nav .dropdown")
        for category in navbar_list:
            category.get_attribute("dropdown-menu")

    def test_logo_href(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#logo > a")))
        href = browser.find_element(By.CSS_SELECTOR, "#logo > a").get_attribute("href")
        assert 'home' in href

    def test_carousel_indicators(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".carousel-indicators")))
        browser.find_element(By.CSS_SELECTOR, ".carousel-indicators")

    def test_content_image_same_href(self, browser):
        """
        Проверка совпадения ссылки на изображении и ссылки в названии товара
        """
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-thumb")))
        href_img = browser.find_element(
            By.CSS_SELECTOR, ".product-thumb .image a"
        ).get_attribute("href")
        href_content = browser.find_element(
            By.CSS_SELECTOR, ".product-thumb .content a"
        ).get_attribute("href")
        assert href_content == href_img
