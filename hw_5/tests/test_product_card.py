from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProductCard:
    def test_change_page_product(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='iPhone 6']")))
        browser.find_element(By.CSS_SELECTOR, "img[alt='iPhone 6']").click()

    def test_check_image(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "img[class='img-thumbnail mb-3']")))

    def test_check_new_price(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".price-new")
        ))

    def test_check_breadcrumb(self, browser):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".breadcrumb")))

    def test_add_to_cart(self, browser):
        """
        Проверка добавления в корзину из карточки товара
        """
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.ID, "button-cart")))
        cart0 = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button").text
        browser.find_element(By.ID, "button-cart").click()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#header-cart > div > button"), "1"))
        cart1 = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button").text
        assert cart1 != cart0



