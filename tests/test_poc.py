from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import pytest
from selenium.webdriver.common.by import By
import os


def test_poc():
    caps_0 = {
      "build": os.getenv("LT_BUILD_NAME"),
      "name": "Test",
      "platform": "Windows 10",
      "browserName": "Chrome",
      "version": "108.0"
    }
    
    caps_1 = {
      "single_test": {
        "browserName": "Chrome",
        "browserVersion": "108.0",
        "LT:Options": {
          "platformName": "Windows 10",
          "project": "Untitled",
          "plugin": "python-pytest"
        }
      }
    }

    caps_2 = {
        "platform" : "Windows 10",
        "browserName" : "Chrome",
        "version" : "95.0",
        "resolution": "1920x1080",
        "name": "LambdaTest python test",
        "build": "LambdaTest python test",
        "video": True,
        "console": True
    }

    executor_0 = os.getenv("LT_HUB_URL")
    executor = os.getenv("LT_GRID_URL")
    chrome_driver = webdriver.Remote(command_executor=executor, desired_capabilities=caps_1)
    chrome_driver.get('https://itaka.pl/')
    chrome_driver.maximize_window()
    chrome_driver\
        .find_element(By.CSS_SELECTOR, "#hotels-switcher-box > div.fBut > button")\
        .click()
    title = "Wyniki Wyszukiwania | ITAKA"
    
    assert title == chrome_driver.title
    chrome_driver.close()
