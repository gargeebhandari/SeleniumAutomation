from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage

def test_InvalidDataRegistration():
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_email("testingworld@mailinator.com")
    driver.close()
