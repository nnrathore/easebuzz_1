from selenium import webdriver
import logging

def getWebDriverInstance(browser):
    """
   Get WebDriver Instance based on the browser configuration

    Returns:
        'WebDriver Instance'
    """
    baseURL = "https://letskodeit.teachable.com/"
    if browser == "edge":
        # Set ie driver
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        # Set chrome driver
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    # Setting Driver Implicit Time out for An Element
    driver.implicitly_wait(3)
    # Maximize the window
    driver.maximize_window()
    # Loading browser with App URL
    driver.get(baseURL)
    log("this is launching web")
    return driver

def log(msg):
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG, filename="text11.log")
    logging.info(msg)