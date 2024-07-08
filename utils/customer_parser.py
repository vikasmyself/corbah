import configparser
from pathlib import Path

configFile = "automation.ini"
configFileDir = "config"
config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
#print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(configFileDir).joinpath(configFile)
#print(CONFIG_FILE)

config.read(CONFIG_FILE)

def getBaseURL():
    return config['corbah']['baseURL']

def getUsername():
    return config['letskodeit']['username']

def getPassword():
    return config['letskodeit']['password']

def getConfig(section,attribute):
    return config[section][attribute]

