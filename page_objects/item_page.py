from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.actionCameras_page import ActionCameras


class ItemPage:

    def __init__(self, driver):
        self.loc_driver = driver
        self.wait = WebDriverWait(self.loc_driver, 8)
        self.action = ActionChains(self.loc_driver)

    buy = (By.XPATH, "//div[@class='prod_price_qty_btns_content']//div[@class='buy_block_content']"
                                       "//form[@id='buy_block']//div[@class='box-info-product']/"
                                       "/div[@class='product_attributes clearfix']/"
                                       "/div[@class='box-cart-bottom']//div//span")

    def add_item(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='prod_price_qty_btns_content']//div[@class='buy_block_content']"
                                       "//form[@id='buy_block']//div[@class='box-info-product']/"
                                       "/div[@class='product_attributes clearfix']/"
                                       "/div[@class='box-cart-bottom']//div//span")))
        element = self.loc_driver.find_element(*ItemPage.buy)
        self.loc_driver.execute_script("arguments[0].click();", element)

    btn = (By.XPATH, "//span[@class='continue button pull-left']")

    def continue_shoping(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='continue button pull-left']")))
        self.loc_driver.find_element(*ItemPage.btn).click()

    menu = (By.XPATH, "//p[@class='cat-title']")

    def hover_menu(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "cat-title")))
        product = self.loc_driver.find_element(*ItemPage.menu)
        self.action.move_to_element(product).perform()

    tv_audio = (By.XPATH, "//span[contains(text(),'ТВ, Аудио & Видео')]")

    def move_to_section(self):
        tv = self.loc_driver.find_element(*ItemPage.tv_audio)
        self.action.move_to_element(tv).perform()

    link_txt = (By.LINK_TEXT, "Спортни екшън камери")

    def select_link(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Спортни екшън камери")))
        self.loc_driver.find_element(*ItemPage.link_txt).click()
        return ActionCameras(self.loc_driver)
