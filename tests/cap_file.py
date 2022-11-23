import os

capabilities = {
  "build" : os.getenv("LT_BUILD_NAME"),
  "name" : os.getenv("LT_BUILD_NAME"),
  "platform" : "Windows 11",
  "browserName" : "Chrome",
  "version" : "101.0"
}
