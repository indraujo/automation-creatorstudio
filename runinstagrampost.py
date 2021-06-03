import pandas as pd
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
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class main():
    def __init__(self):
        print("***** Welcome to Google keyword downloader! *****")
        firefox = "C:/Users/Indra/Documents/GitHub/automation-shopee/drivers/geckodriver.exe"
        '''self.options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=self.options, 
        desired_capabilities=self.options.to_capabilities(), 
        executable_path=self.chromedriver)'''
        #bin = FirefoxBinary('C:\\Users\\Indra\\Documents\\GitHub\\automation-shopee\\drivers')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.post = PosttoInstagramFeed(self.driver)
        self.t = testmods(self.driver)

    def mains(self):
        global time
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
            df = pd.read_excel(".\\modules\\facebookcreatorstudio\\postdata.xlsx",sheet_name="Sheet1")
            account = df["account"].tolist()
            path = df["path"].tolist()
            image1 = df["image1"].tolist()
            image2 = df["image2"].tolist()
            image3 = df["image3"].tolist()
            image4 = df["image4"].tolist()
            image5 = df["image5"].tolist()
            image6 = df["image6"].tolist()
            image7 = df["image7"].tolist()
            image8 = df["image8"].tolist()
            image9 = df["image9"].tolist()
            caption = df["caption"].tolist()
            date = df["date"].tolist()
            times = df["time"].tolist()
            print(df)
            print(len(df))
            for i in range(len(df)):
                print("Account : ",account[i])
                #print("Caption : ",caption[i])
                print("Day     : ",date[i].day)
                print("Month     : ",date[i].strftime('%B'))
                print("Year     : ",date[i].year)
                print("Time Hour : ",times[i].hour)
                print("Time minutes : ",times[i].minute)
                print("Time AM/PM : ",times[i].strftime("%p"))
                print()
                
                image = []
                if pd.notna(image1[i]):
                    image.append(path[i]+image1[i]+".jpg")
                if pd.notna(image2[i]):
                    image.append(path[i]+image2[i]+".jpg")
                if pd.notna(image3[i]):
                    image.append(path[i]+image3[i]+".jpg")
                if pd.notna(image4[i]):
                    image.append(path[i]+image4[i]+".jpg")
                if pd.notna(image5[i]):
                    image.append(path[i]+image5[i]+".jpg")
                if pd.notna(image6[i]):
                    image.append(path[i]+image6[i]+".jpg")
                if pd.notna(image7[i]):
                    image.append(path[i]+image7[i]+".jpg")
                if pd.notna(image8[i]):
                    image.append(path[i]+image8[i]+".jpg")
                if pd.notna(image9[i]):
                    image.append(path[i]+image9[i]+".jpg")

                postdata = {
                    'account' : account[i],
                    'caption' : caption[i],
                    'image'   : image,
                    'schedule': {
                        'day'  : str(date[i].day),
                        'month': str(date[i].strftime('%B')),
                        'year' : str(date[i].year),
                        'hour' : str(times[i].hour),
                        'minute': str(times[i].minute),
                        'ampm' : str(times[i].strftime("%p"))
                    }

                }

                self.post.clickCreatePost()
                self.post.clickCreatePostInstagramFeed()
                self.post.selectInstagramAccount(account[i])
                self.t.inputkey(postdata)
                time.sleep(30)
        
        self.post.clickUser()
        self.post.clickLogOut()
        self.driver.quit()

if __name__ == "__main__":
    m = main()
    m.mains()