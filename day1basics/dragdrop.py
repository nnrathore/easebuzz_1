from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import logging
class DragAndDrop():

    def test1(self,driver,xpath_dragger, xpatth_dropper):

        drager = driver.find_element(By.XPATH, xpath_dragger)
        dropper = driver.find_element(By.XPATH, xpatth_dropper)
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(drager, dropper).perform()
            # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag And Drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")

ff = DragAndDrop()
ff.test1()