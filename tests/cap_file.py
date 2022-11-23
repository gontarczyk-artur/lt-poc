import os

capabilities = {
  "browserName": "Firefox",
  "browserVersion": "106.0",
  "LT:Options": {
    "username": os.getenv("LT_USERNAME"),
    "accessKey": os.getenv("LT_ACCESS_KEY"),
    "platformName": "Windows 10",
    "project": "Untitled"
  }
}
