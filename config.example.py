from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform

# selenium_driver     = webdriver.Firefox()
user = {"username": "CHANGEME", "password": "CHANGEME"}


def get_web_driver():
    # sets up driver to run without opening window Remove to see process
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    if platform.system() == "Windows":
        return webdriver.Chrome("./chromedriver.exe")  # options=options
    else:
        return webdriver.Chrome("./chromedriver")  # options=options
