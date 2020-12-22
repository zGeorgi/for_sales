from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities

from data_for_tests.for_sale_testData import DataForSaleTest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="choose desire browser from cmd"
    )


@pytest.fixture(scope="class")
def invoke_browser(request):
    global driver
    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        chr_oprions = webdriver.ChromeOptions()
        #driver = webdriver.Remote("http://ec2-18-134-74-167.eu-west-2.compute.amazonaws.com:4444", options=chr_oprions)
        # driver = webdriver.Remote("http://172.17.0.1:4444/") # this is for localhost
        # chr_oprions = webdriver.ChromeOptions() 
        driver = webdriver.Remote(command_executor="http://ec2-18-130-247-36.eu-west-2.compute.amazonaws.com:4444/wd/hub",
            options=chr_oprions)
        # driver = webdriver.Remote("http://ec2-35-178-116-17.eu-west-2.compute.amazonaws.com:4444", options=chr_oprions)
    if browser == "firefox":
        f_opt = webdriver.FirefoxOptions()
        driver = webdriver.Remote("http://ec2-35-178-116-17.eu-west-2.compute.amazonaws.com:4444", options=f_opt)
        # driver = webdriver.Firefox(executable_path="/home/georgi/geckodriver/geckodriver")
    if browser == "opera":
        opera_opt = webdriver.ChromeOptions()
        driver = webdriver.Remote("http://ec2-35-178-116-17.eu-west-2.compute.amazonaws.com:4444", options=opera_opt)

    driver.get("https://4sales.bg")
    print(driver.title)
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.quit()

@pytest.fixture(params=DataForSaleTest.data)
def load_data(request):
    return request.param
