import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture(scope='class')
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info","browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__('edge'):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name from the list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
