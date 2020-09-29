from selenium.webdriver.common.by import By


class Basket:

    def __init__(self, driver):
        self.loc_driver = driver

    btn = (By.XPATH, "//div[@class='shopping_cart clearfix']")

    def open_basket(self):
        self.loc_driver.find_element(*Basket.btn).click()

    quantity = (By.CSS_SELECTOR, "span[class='quantity-formated'] span[class='quantity']")

    def get_quantity(self):
        txt = self.loc_driver.find_element(*Basket.quantity).text
        return int(txt)

    cl = (By.CSS_SELECTOR, ".close_cart_block")

    def close_basket(self):
        self.loc_driver.find_element(*Basket.cl).click()
