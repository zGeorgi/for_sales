from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.item_page import ItemPage


class HomePage:

    def __init__(self, driver):
        self.loc_driver = driver
        self.wait = WebDriverWait(self.loc_driver, 5)

    btn = (By.XPATH, "//button[@id='onesignal-slidedown-cancel-button']")

    def refuse_notifications(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[@id='onesignal-slidedown-cancel-button']")))
        self.loc_driver.find_element(*HomePage.btn).click()

    coki = (By.XPATH, "//tbody/tr/td[2]/span")

    def accept_cookiies(self):
        cook = self.loc_driver.find_element(*HomePage.coki)
        # js execute
        self.loc_driver.execute_script("arguments[0].click();", cook)

    input_field = (By.ID, "search_query_block")

    def search_items(self, key_word ):
        self.loc_driver.find_element(*HomePage.input_field).send_keys(key_word)

    search_icon = (By.XPATH, "//i[@class='fa fa-search']")

    def click_search(self):
        element = self.loc_driver.find_element(*HomePage.search_icon)
        action = ActionChains(self.loc_driver)
        action.move_to_element(element).click().perform()

    item_ = (By.XPATH, "//a[contains(text(),'волан American eagle ')]")

    def choose_item(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'волан American eagle ')]")))
        self.loc_driver.find_element(*HomePage.item_).click()
        return ItemPage(self.loc_driver)
