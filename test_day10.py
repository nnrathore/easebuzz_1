"""
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import time

from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import selenium
"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

# logging.basicConfig(level=logging.INFO, filename="demolog.log")
logging.error("this is an examplee of error")
logging.debug('this is an example of debug')
logging.info("this is an example of infoo")
logging.critical("this is an example of critical")
logging.warning("this is an examle of warning")

import pytest
import allure
baseUrl = "https://courses.letskodeit.com/practice"

    # logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
    #                     datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG,filename="text.log")

    # logging.basicConfig(filename="df.log")
def test_lkogig():
    print("hhhh")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    logging.warning("warning message")
    logging.info("info message")
    logging.error("error message")
    logging.debug("debug msg")
    logging.critical("critical")

@allure.description("this test will be for demo")
@allure.title("Open application")
@allure.severity(allure.severity_level.MINOR)

def test_1():
    baseUrl = "https://courses.letskodeit.com/practice"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    row = len(driver.find_elements(By.XPATH,'//*[@id="product"]/tbody/tr'))
    col = len(driver.find_elements(By.XPATH, '//*[@id="product"]/tbody/tr/th'))
    allure.attach(driver.get_screenshot_as_png(), name='test demo', attachment_type=AttachmentType.PNG)
    driver.get("https://google.com")
    time.sleep(5)
    print(row)
    print(col)
# import pytest
# import allure
# class test_allure():
#     def test_1(self):
#         pytest.skip("gggg")
#         print("Hello 1")
#         assert True
#     def test_2(self):
#         print("Hello 2")
#
#     def test_3(self):
#         print("Hello 3")