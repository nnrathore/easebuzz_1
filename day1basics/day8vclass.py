from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

baseUrl = "https://jqueryui.com/droppable/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)

driver.switch_to.frame(0)
so = driver.find_element(By.ID,"draggable")
De = driver.find_element(By.ID,"droppable")
# mouse_hover = driver.find_element(By.XPATH,"//*[@id='mousehover']")
mouse_mov = ActionChains(driver)
mouse_mov.click_and_hold(so).release(De).perform()

time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='mouse-hover-content']/a[2]").click()

# Total_col = len(driver.find_elements(By.XPATH,"//table[@id='product']/tbody/tr/th"))

# print(Total_col)
# print(Total_Row)x`

# for r in range(2,Total_Row+1):
#     read_col_val = driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr[" + str(r) + "]/td[" + str(2) +"]").text
#     if read_col_val == "Selenium WebDriver With Java":
#         print(driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr[" + str(r) + "]/td[3]").text)

# print("total row %s, tptal col %s" %(Total_col,Total_Row)
# print("//table[@id='product']+ str(c) + /tbody")

driver.find_element(By.XPATH,'//*[@id="openwindow"]')

