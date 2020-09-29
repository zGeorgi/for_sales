from selenium import webdriver
import pytest

from data_for_tests.for_sale_testData import DataForSaleTest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="choose desire browser from cmd"
    )

@pytest.fixture(scope="class")
def invoke_browser(request):
    global driver
    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="/home/georgi/chromedriver/chromedriver")
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path="/home/georgi/geckodriver/geckodriver")

    driver.get("https://4sales.bg/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture(params=DataForSaleTest.data)
def load_data(request):
    return  request.param