from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCatalogCamera:
    def test_change_page(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#narbar-menu")))
        browser.find_element(By.PARTIAL_LINK_TEXT, "Cameras").click()

    def test_check_breadcrumb(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".breadcrumb")))

    def test_content(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#content > h2")))

    def test_sort_by(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".input-group-text")))

    def test_list_group(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".list-group")))

