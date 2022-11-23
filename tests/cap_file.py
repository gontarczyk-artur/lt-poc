import os

capabilities = {
	"browserName": os.getenv("LT_BROWSER_NAME") or "Firefox",
	"browserVersion": os.getenv("LT_BROWSER_VERSION") or "102.0",
	"LT:Options": {
		"platformName": os.getenv("LT_PLATFORM") or "Windows 10",
		"project": "Untitled",
		"w3c": True
	}

}
