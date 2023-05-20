from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope='class', autouse=True)
def class_setup_teardown():
    print('start of class')
    yield
    print('end of class')


@pytest.fixture(scope='function', autouse=True)
def test_setup_teardown(request):
    print('start of the test')
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_page_load_timeout(10)

    yield driver

    driver.quit()

    print('end of the test')
