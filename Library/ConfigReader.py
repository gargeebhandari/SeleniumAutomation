import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    # config.read("../ConfigurationFiles/Config.cfg")
    # above line for executing relative to file the in relative path ony single dot will be there
    config.read("./ConfigurationFiles/Config.cfg")

    # above line is when we are executing the file at project level
    return config.get(section, key)


#print(readConfigData('Details', 'Application_URL'))

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)

#print(fetchElementLocators('Registration', 'username_name'))
