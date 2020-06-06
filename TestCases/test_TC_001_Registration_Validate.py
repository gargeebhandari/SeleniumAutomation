from selenium. webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
from DataGenerator import DataGen
import pytest
import openpyxl


@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    driver.close()


