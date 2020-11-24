from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities

from data_for_tests.for_sale_testData import DataForSaleTest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="choose desire browser from cmd"
    )

 # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
@pytest.fixture(scope="class")
def invoke_browser(request):
    global driver
    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        #chr_options = webdriver.ChromeOptions()
        # chr_options.add_argument("--headless")
        #chr_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver", options=chr_options)
        driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="/home/georgi/geckodriver/geckodriver")

    driver.get("https://4sales.bg")
    print(driver.title)
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture(params=DataForSaleTest.data)
def load_data(request):
    return request.param
