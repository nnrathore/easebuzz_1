from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.select import Select
class SwitchToWindow():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        drivr = 10
        webdriver.Chrome().get()
        webdriver.Chrome().title
        driver.maximize_window()
        driver.get(baseUrl)

        print(driver.find_element(By.ID, "enabled-example-input").is_enabled())
        driver.find_element(By.ID,"disabled-button").click()
        print(driver.find_element(By.ID, "enabled-example-input").is_enabled())



        # driver.find_element(By.ID,"alertbtn").click()
        # time.sleep(2)
        # driver.switch_to.alert.accept()

        #
        # driver.find_element(By.ID, "confirmbtn").click()
        # time.sleep(2)
        # driver.switch_to.alert.dismiss()



        # print(driver.find_element(By.ID, "bmwradio").is_selected())
        # time.sleep(2)
        # print(driver.find_element(By.ID, "benzcheck").is_selected())
        # time.sleep(2)

        # sel = Select(driver.find_element(By.ID,"multiple-select-example"))
        # time.sleep(2)
        # sel.select_by_index(0)
        # time.sleep(2)
        # sel.select_by_value("peach")
        # driver.execute_script("window.scrollBy(0, 1000)");
        # time.sleep(5)
        #
        #
        #
        # driver.switch_to.frame(0)

        # print(driver.current_window_handle)
        #
        # # Find parent handle -> Main Window
        # parentHandle = driver.current_window_handle
        # print("Parent Handle: " + parentHandle)
        #
        # # Find open window button and click it
        # driver.find_element(By.ID, "opentab").click()
        # time.sleep(2)
        #
        # # Find all handles, there should two handles after clicking open window button
        # handles = driver.window_handles
        # for i in handles:
        #     print(i)
        #     if i not in parentHandle:
        #         driver.switch_to.window(i)
        # #
        #
        #
        # # Switch to window and search course
        # for handle in handles:
        #     print("Handle: " + handle)
        #     if handle not in parentHandle:
        #         driver.switch_to.window(handle)
        #         print("Switched to window:: " + handle)
        # driver.find_element(By.CLASS_NAME, "zen-course-thumbnail").click()
        # searchBox.send_keys("python")
        time.sleep(2)
        # driver.close()
        # break

        # Switch back to the parent handle
        # driver.execute_script("window.scrollBy(0,-1000)")
        # time.sleep(5)
        # driver.switch_to.default_content()
        # x=driver.find_element(By.ID, "carselect")
        # sel = Select(x)
        # sel.select_by_value("honda")
        # time.sleep(2)
        # sel.select_by_visible_text("Benz")
        # time.sleep(2)

        driver.execute_script("window.scrollBy(0,-1000)")







ff = SwitchToWindow()
ff.test()