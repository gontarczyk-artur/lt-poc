import os

browser_name: str = os.getenv("LT_BROWSER_NAME")

capabilities = {
	"browserName": browser_name,
	"browserVersion": "102.0",
	"LT:Options": {
		"platformName": "Windows 10",
		"project": "Untitled",
		"w3c": True
	}

}
