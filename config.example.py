from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

#selenium_driver     = webdriver.Firefox()
users = [["user","user_password"],
        #["simonesolskind","3Jh!h9SjU7Bvfdsf786"]
        ]


def get_web_driver():
       #sets up driver to run without opening window Remove to see process
   # options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    return webdriver.Chrome('./chromedriver.exe')#options=options
