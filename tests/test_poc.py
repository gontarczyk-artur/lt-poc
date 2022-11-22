from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import pytest
from selenium.webdriver.common.by import By
import os


def test_poc():
    caps = {
      "build": os.getenv("LT_BUILD_NAME"),
      "name": "Test",
      "platform": "Windows 10",
      "browserName": "Chrome",
      "version": "108.0"
    }

    executor = os.getenv("LT_HUB_URL")
    chrome_driver = webdriver.Remote(command_executor=executor, desired_capabilities=caps)
    chrome_driver.get('https://itaka.pl/')
    chrome_driver.maximize_window()
    chrome_driver\
        .find_element(By.CSS_SELECTOR, "#hotels-switcher-box > div.fBut > button")\
        .click()
    title = "Wyniki Wyszukiwania | ITAKA"
    
    assert title == chrome_driver.title
    chrome_driver.close()
