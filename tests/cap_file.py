import os

capabilities = {
	"browserName": os.getenv("LT_BROWSER_NAME"),
	"browserVersion": os.getenv("LT_BROWSER_VERSION"),
	"LT:Options": {
		"platformName": os.getenv("LT_PLATFORM"),
		"project": "Untitled",
		"w3c": True
	}

}
