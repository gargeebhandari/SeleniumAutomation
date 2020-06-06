from selenium import webdriver
from Library import ConfigReader


def startBrowser():
    global driver
    if ((ConfigReader.readConfigData('Details', 'Browser')) == 'chrome'):
        #driver = webdriver.Chrome("./Driver/chromedriver.exe")
        driver = webdriver.Chrome("C:/Users/Admin/Downloads/Python class docs/chromedriver_win32/chromedriver.exe")

    elif ((ConfigReader.readConfigData('Details', 'Browser')) == 'firefox'):
        driver = webdriver.Firefox(executable_path="C:/Users/Admin/Downloads/Python class docs/geckodriver-v0.26.0-win64/geckodriver.exe")
    else:
        driver = webdriver.Chrome("C:/Users/Admin/Downloads/Python class docs/chromedriver_win32/chromedriver.exe")

    # driver.get("https://www.thetestingworld.com/testings/")
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver


def closeBrowser():
    driver.close()
