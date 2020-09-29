from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ActionCameras:

    def __init__(self, driver):
        self.loc_driver = driver

    item_number = (By.CSS_SELECTOR, ".heading-counter")

    def displayed_quantity(self):
        wait = WebDriverWait(self.loc_driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".heading-counter")))

        text = self.loc_driver.find_element(*ActionCameras.item_number).text
        # extract digit from string
        slices = text.split()
        num = 0
        for i in slices:
            if i.isdigit():
                num = int(i)
                break
        return num

    containers = (By.XPATH, "//div[@class='content_product_list hide-productdes"
                                                      " hide-coloroption hide-stockinfo ']/ul/li")

    def count_items(self):
        lis = self.loc_driver.find_elements(*ActionCameras.containers)
        return len(lis)
