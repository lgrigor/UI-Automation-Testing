from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from _pytest.runner import runtestprotocol

import pytest
import time
import sys
import os
import re

import allure
from allure_commons.types import AttachmentType

root = os.path.abspath(os.path.join(os.path.dirname(__file__), r"..\.."))
sys.path.append(root)


@pytest.fixture(scope='class', autouse=True)
def class_setup_teardown():
    print('Suite Setup')

    yield

    print('Suite TearDown')


@pytest.fixture(scope='function', autouse=True)
def test_setup_teardown(request):
    print('Test Setup')

    # Chrome driver initialization
    driver = initialize_chrome()

    yield driver

    print('\nTest TearDown')

    # Take a screenshot before closing the browser
    take_screenshot(driver=driver, test_name=request.node.name)

    # Close the browser
    driver.quit()


def initialize_chrome():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(10)
    return driver


def take_screenshot(driver, test_name):
    match = re.search(r"^test_(.*)_(\d+)\[?(.*?)]?$", test_name)
    if match.group(3):
        screenshot_path = rf"{root}\Results\{match.group(2)}_{match.group(1)}__{match.group(3)}_screenshot.png"
    else:
        screenshot_path = rf"{root}\Results\{match.group(2)}_{match.group(1)}_screenshot.png"

    os.environ["TestScreenshot"] = screenshot_path
    driver.save_screenshot(screenshot_path)


def pytest_runtest_protocol(item):
    reports = runtestprotocol(item)
    for report in reports:
        if report.when == "call":
            time.sleep(0.5)
            screenshot_path = os.getenv("TestScreenshot")

            if screenshot_path:

                if report.outcome == "passed":
                    os.remove(screenshot_path)
                elif report.outcome == "failed":
                    allure.attach.file(source=screenshot_path, name="Fail Screen", attachment_type=AttachmentType.PNG)
                else:
                    print(f"Conftest-Warning: Unhandled outcome - {report.outcome}")

            else:
                print(f"Conftest-Warning: Screenshot wasn't find - {screenshot_path}")

    ihook = item.ihook
    ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)
    return True
