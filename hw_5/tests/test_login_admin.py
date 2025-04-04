from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginAdmin:
    def test_change_page_product(self, browser):
        browser.get(browser.url + "/administration")

    def test_check_logo_img(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "img[title='OpenCart']")))

    def test_check_username(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#input-username")))

    def test_check_password(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#input-password")))

    def test_check_button_login(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")
        ))
