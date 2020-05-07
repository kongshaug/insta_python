import config as cfg
import time
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
import matplotlib.pyplot as plt
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy import create_engine
import csv_connection


class instagram_bot:
    def __init__(self, hashtag):

        user = cfg.user
        self.username = user["username"]
        self.password = user["password"]
        self.driver = cfg.get_web_driver()
        self.hashtag = hashtag

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.driver.find_element_by_class_name("hztqj").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//option[contains(text(), 'Dansk')]")[
            0
        ].click()
        print("changed to danish")
        time.sleep(3)
        self.driver.find_elements_by_class_name("_2hvTZ")[0].send_keys(self.username)
        self.driver.find_elements_by_class_name("_2hvTZ")[1].send_keys(self.password)
        print("put credentials")
        time.sleep(2)
        self.driver.find_element_by_class_name("L3NKy").click()
        print("you.are.in")

    def tear_down(self):
        print("selfdestruct in:")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        self.driver.quit()
        print("mission.complete")

    def search(self):
        self.driver.get("https://www.instagram.com/explore/tags/" + self.hashtag)

    def get_images(self, image_len=100):
        self.login()
        time.sleep(5)

        images = []
        self.search()
        while len(images) < image_len:

            for post in self.driver.find_elements_by_class_name("KL4Bh"):
                all_images = post.find_element_by_tag_name("img").get_attribute(
                    "srcset"
                )

                img_with_width = all_images.split(",")[2]
                img = img_with_width.split(" ")[0]
                images.append(img)

            print("Number of images ready to download: {} ".format(len(images)))
            self.scroll()

        time.sleep(5)
        self.tear_down()

        conv_images = self.convert_images(images)
        csv_connection.save_to_CSV(conv_images, self.hashtag)

    def scroll(self):
        for i in range(6):  # adjust integer value for need
            # you can change right side number for scroll convenience or destination
            self.driver.execute_script("window.scrollBy(0, 1400)")
            # you can change time integer to float or remove
            time.sleep(4)

    def convert_images(self, images):
        conv_images = []
        for image in images:

            array_image = io.imread(image)
            array_image = resize(array_image, (96, 96, 3))
            gray = rgb2gray(array_image)
            conv_images.append(gray)
            time.sleep(0.5)
            print("image nr {} converted".format(len(conv_images)))

        return conv_images

