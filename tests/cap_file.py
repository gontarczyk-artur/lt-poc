import os

capabilities = {
  "single_test": {
    "browserName": "Firefox",
    "browserVersion": "106.0",
    "LT:Options": {
      "username": os.getenv("LT_USERNAME"),
      "accessKey": os.getenv("LT_ACCESS_KEY"),
      "platformName": "Windows 10",
      "project": "Untitled",
      "selenium_version": "4.0.0",
      "w3c": True,
      "plugin": "python-pytest"
    }
  }
}
