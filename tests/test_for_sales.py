from time import sleep

from page_objects.basket_page import Basket
from page_objects.home_page import HomePage
from utilities.base_class import BaseClass


class TestForSale(BaseClass):

    def test_sale(self, load_data):
        loger = self.logger_object()

        home_page = HomePage(self.driver)
        home_page.refuse_notifications()
        home_page.accept_cookiies()
        loger.info("Stop notification and accept cookies")

        home_page.search_items(load_data["product"])
        home_page.click_search()
        loger.info("Search items")

        item_page = home_page.choose_item()
        sleep(2)
        item_page.add_item()
        loger.info("Select item and add it to the Basket!")

        item_page.continue_shoping()
        item_page.hover_menu()
        item_page.move_to_section()
        action_camera = item_page.select_link()
        loger.info("Open other products!")

        num = action_camera.displayed_quantity()
        containers = action_camera.count_items()
        loger.info("compare displayed quantity and items on the page")

        assert containers == num

        basket = Basket(self.driver)
        loger.info("Open the Basket and get the quantity of the items!")
        basket.open_basket()
        quantity = basket.get_quantity()
        self.driver.get_screenshot_as_file("/home/georgi/PycharmProjects/forSales/reports/basket.png")
        loger.info("compare received quantity with desired and close the Basket!")
        assert quantity == 1
        basket.close_basket()
