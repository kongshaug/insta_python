import config as cfg
import time
import cv2
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
import matplotlib.pyplot as plt
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy import create_engine




class instagram_bot:

    def __init__(self, hashtag):
       
        user = cfg.user
        self.username = user["username"]
        self.password = user["password"]
        self.driver = cfg.get_web_driver()

        self.login()
        time.sleep(5)
        self.images = self.get_images(hashtag, 5)

        time.sleep(5)
        #self.tear_down()


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        self.driver.find_element_by_class_name("hztqj").click()  
        time.sleep(2)
        self.driver.find_elements_by_xpath("//option[contains(text(), 'Dansk')]")[0].click()
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
    
    def search(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/'+ hashtag)

    def get_images(self, hashtag, image_len=100):
        images = []
        self.search(hashtag)
        while len(images) <= image_len:
        
            for post in self.driver.find_elements_by_class_name("KL4Bh")[9:12]:
                images = post.find_element_by_tag_name("img").get_attribute("srcset")
    
                img_with_width = images.split(",")[2]               
                img = img_with_width.split(" ")[0]
                images.append(img)
        
            self.scroll()
            
        return self.convert_images(images)
        
    def scroll(self):
         for i in range(6): # adjust integer value for need
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
            time.sleep(4)
            print("image nr {} converted".format(len(conv_images)))
        return conv_images
    
    def save_to_db(self, images):
        con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
        engine = create_engine(con_str)


            


    
        
