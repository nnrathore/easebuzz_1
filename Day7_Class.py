"""
Xpath
Css selector
Select Function
Switch to window
Switch to Tab
Switch to Frame

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
import os
from selenium.webdriver.support.select import Select
import pytest
import allure
class radiobutton():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        row = len(driver.find_elements(By.XPATH,'//*[@id="product"]/tbody/tr'))
        col = len(driver.find_elements(By.XPATH, '//*[@id="product"]/tbody/tr/th'))
        print(row)
        print(col)
        for i in range(2,row+1):
            for j in range(1,col+1):
                print(driver.find_element(By.XPATH, '//*[@id="product"]/tbody/tr[' + str(i) + ']/td[' +  str(j) + ']').text)
        driver.find_element(By.ID,"hide-textbox").click()
        time.sleep(2)
        driver.find_element(By.ID, "show-textbox").click()
        time.sleep(2)
        print(driver.find_element(By.ID,'displayed-text').send_keys("hgjjg"))
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1000)")
        time.sleep(3)
        element = driver.find_element(By.ID, "mousehover")
        # driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # time.sleep(2)
        # driver.execute_script("window.scrollBy(0, -150);")
        # time.sleep(3)
        # Native Way To Scroll Element Into View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        # print("Location: " + str(location))
        # driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(3)


    # driver.switch_to.frame(2)
        # mouse = ActionChains(driver)
        # time.sleep(2)
        # a= driver.find_element(By.XPATH,'//*[@id="draggable"]')
        # b= driver.find_element(By.XPATH,'//*[@id="droppable"]/p')
        # mouse.drag_and_drop(a,b).perform()
        # mouse.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
        # mouse.move_to_element(driver.find_element(By.XPATH,"//*[@id='mouse-hover-example-div']//a[2]")).click().perform()
        # print(driver.find_element(By.ID,"opentab").get_attribute("href"))
        # time.sleep(5)
        # # driver.find_element(By.ID,'name').send_keys("Nilesh")
        # driver.find_element(By.ID,'alertbtn').click()
        # time.sleep(3)
        # driver.switch_to.alert.accept()
        # time.sleep(3)
        # driver.find_element(By.ID, 'name').send_keys("Nilesh")
        # driver.find_element(By.ID,'confirmbtn').click()
        # time.sleep(3)
        # driver.switch_to.alert.dismiss()
        # time.sleep(3)



"""
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

r= radiobutton()
# r.test()
"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
# import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG,filename="text.log")

# logging.basicConfig(filename="text.log", level=logging.DEBUG, format=)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")