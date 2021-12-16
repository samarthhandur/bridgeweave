
from appium import webdriver
import unittest
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def initial_set():
        desired_capabilities= dict(
                platformName='Android',
                deviceName="Samarth's Note 9 Pro",
                udid='9ee04236',
                platformVersion='10',
                appActivity='investorai.features.splash.ui.SplashHostActivity',
                appPackage= 'com.bridgeweave.investorai',
                noReset='false'
                )
        global driver	
        driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
        driver.implicitly_wait(15)
       

def login():
            driver.find_element_by_id(get_property('EMAIL_FIELD')).send_keys(get_property('EMAIL'))
            driver.find_elements_by_class_name(get_property('PASSCODE_FIELD'))[1].send_keys(get_property('PASSCODE'))
            driver.find_element_by_id(get_property('SUBMIT_BTTN')).click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, get_property('WELCOME_TITLE'))))
            return driver.find_element_by_id(get_property('WELCOME_TITLE')).is_displayed()
        
def skip_terms():
            driver.find_element_by_id(get_property('SKIP_WELCOME')).click()
            driver.implicitly_wait(2)
            driver.find_element_by_id(get_property('SKIP_TERMS')).click()
            driver.implicitly_wait(2)
            driver.find_element_by_id(get_property('SKIP_BIOMETRIC_AUTH')).click()
    
def wait_explicit( sec,identifier):
        	WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.ID, identifier)))
    
def find_element( idenitfier):
        return driver.find_element_by_id(idenitfier)

def key_press(code):
        driver.press_keycode(code)

def load_properties(filepath, sep='=', comment_char='#'):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(comment_char):
                    key_value = line.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
    return props

def get_property(prop):
        property_file = os.path.join(os.getcwd(), "elements.properties")
        env_params=load_properties(filepath=property_file)
        return env_params[prop]
        
def tearDown():
        driver.quit()