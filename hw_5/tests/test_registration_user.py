from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationUser:
    def test_change_page_account(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
        browser.find_element(By.CSS_SELECTOR, ".nav li:nth-child(2) > div > a").click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
            By.PARTIAL_LINK_TEXT, "Register")))
        browser.find_element(By.PARTIAL_LINK_TEXT, "Register").click()

    def test_check_column_right(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#column-right")))

    def test_personal_details(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#account")))

    def test_checkbox(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-newsletter")))

    def test_check_continue(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")))
