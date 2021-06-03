from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from modules.facebookcreatorstudio.instagramcontentpostsPage import PosttoInstagramFeed
class testmods():
    def __init__(self,setup):
        self.driver = setup
        self.post = PosttoInstagramFeed(self.driver)

    def scheduleFacebook(self,schedule):
        self.post.clickPostFacebook()
        self.post.clickScheduleFacebook()
        self.post.clickOptionScheduleFacebook()
        self.post.setSchedule(schedule)
        self.post.clickScheduleFacebook()


    def scheduleInstagram(self,schedule):
        self.post.clickScheduleInstagram()
        self.post.clickOptionScheduleInstagram()
        self.post.setSchedule(schedule)
        self.post.clickScheduleInstagram()

    def inputkey(self,key):
        #imgpath = "E:\\HIJABSIMPLE\\katalog\\wm\\photo_1598@01-02-2021_12-42-06.jpg"
        caption = key.get("caption")
        imgpath = key.get("image")
        schedule_datetime = key.get("schedule")
        self.post.inputCaption(caption)

        for i in range(len(imgpath)):
            self.post.inputImage(imgpath[i])

        self.scheduleFacebook(schedule_datetime)

        self.scheduleInstagram(schedule_datetime)

        self.post.clickSchedule()

        notification = self.post.getNotificationSuccessfullySchedule()
        if notification == True:
            print("success")
        else:
            print("not success")