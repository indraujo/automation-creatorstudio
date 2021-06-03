import sys,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

from modules.facebookcreatorstudio.instagramcontentpostsMod import testmods
from modules.facebookcreatorstudio.instagramcontentpostsPage import PosttoInstagramFeed



class main():
    def __init__(self):
        print("***** Welcome to Google keyword downloader! *****")
        print("***** Please input your keyword *****")
        self.chromedriver = ".\\Drivers\\chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=self.options, 
        desired_capabilities=self.options.to_capabilities(), 
        executable_path=self.chromedriver)
        self.driver.maximize_window()
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.post = PosttoInstagramFeed(self.driver)
    
    def main(self):
        
        
        self.driver.get("https://business.facebook.com/creatorstudio/home")
        self.driver.get("https://www.facebook.com/login/?next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo")
        time.sleep(3)
        username = "indraujo"
        password = "chuvenk3"
        input_username_xpath = "//input[@id='email']"
        input_password_xpath = "//input[@id='pass']"
        button_login_xpath = "//button[@id='loginbutton']"

        self.driver.find_element(By.XPATH,input_username_xpath).send_keys(username)
        self.driver.find_element(By.XPATH,input_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH,button_login_xpath).click()
        time.sleep(5)
        instagrambar_xpath = "//div[@id='media_manager_chrome_bar_instagram_icon']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,instagrambar_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,instagrambar_xpath).click()
        
        command = ""
        while command != "exit":
            
            command = input("command : ")
            

            if command == "exit":
                self.driver.close()
            else:
                
                account = "hijabsimple.inc"
                self.post.clickCreatePost()
                self.post.clickCreatePostInstagramFeed()
                self.post.selectInstagramAccount(account)
                t = testmods(self.driver)
                t.inputkey(command)

if __name__ == "__main__":
    m = main()
    m.main()