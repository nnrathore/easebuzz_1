import time
import os
from Demo1 import funDemo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Locaters import payout
print(payout.express_settl.login["xpath_radio_bmw"])


def take_screenshot(driver,Functionality,testname):
    location_SS = "C:\\Users\\USER\\Desktop\\day6\\"
    print(location_SS + Functionality +  "\\" + testname)
    if os.path.isdir(location_SS + Functionality +  "\\" + testname) is None:
        os.mkdir(location_SS + Functionality +  "\\" + testname)
        driver.save_screenshot(location_SS + Functionality +  "\\" + testname + "\\" + "easebuzz_" +str(round(time.time())) + ".png")

print(time.time())


driver = webdriver.Chrome()
driver.get("https://courses.letskodeit.com/practice")
print(driver.title)
# driver.find_element(By.XPATH,"payout.express_settl.login["xpath_radio_bmw"]").click()
take_screenshot(driver, "Payouts", "test1")
driver.close()
# driver.save_screenshot("C:\\Users\\USER\\Desktop\\day6\\login.png")
#
# driver.save_screenshot("C:\\Users\\USER\\Desktop\\day6\\login_" + str(time.time()) + ".png")
#
#
#





# print(funDemo.carss.ob["fname"])
# obj = {"xpath_radio_bmw":"//input[@id='bmwradio']"}
#
# driver.find_element(By.XPATH, obj["xpath_radio_bmw"]).click()

#
# def scrrn(driver):
#     location_ss="C:\\Users\\USER\\Desktop\\day6\\"
#     driver.save_screenshot(location_ss+str(round(time.time()))+".png")
#
# height = driver.execute_script("return window.innerHeight;")
# width = driver.execute_script("return window.innerWidth;")
# print("Height: " + str(height))
# print("Width: " + str(width))
# driver.execute_script("window.scrollBy(0,1000)")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,-100)")
# time.sleep(3)
#
# driver.find_element(By.XPATH,)
#
# element = driver.find_element(By.ID, "mousehover")
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, -150);")
#
#
# scrrn(driver)
# driver.close()
