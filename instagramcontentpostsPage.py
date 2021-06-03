from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

class PosttoInstagramFeed():
    def __init__(self,setup):
        self.driver = setup

    def inputCaption(self,key):
        JS_ADD_TEXT_TO_INPUT = """
            var elm = arguments[0], txt = arguments[1];
            elm.value += txt;
            elm.dispatchEvent(new Event('change'));
            """

        caption_xpath = "//div[@class='notranslate _5rpu' and @role='combobox']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,caption_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,caption_xpath).send_keys(key)
            #self.driver.execute_script(JS_ADD_TEXT_TO_INPUT, caption_xpath, key)

    def inputImage(self,key):
        button_addcontent_xpath = "//div[@class='_82ht']//button[@class='accessible_elem _5f0v']"
        input_content_xpath = "//input[@class='_n _5f0v']"
        
        time.sleep(1)
        
        button_add = self.driver.find_element_by_xpath(button_addcontent_xpath)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);",button_add)
        self.driver.execute_script("arguments[0].click();", button_add)
        #button_add.click()
        element = self.driver.find_element_by_xpath(input_content_xpath)
        element.send_keys(key)
        #self.driver.execute_script(f"arguments[0].innerText = '{key}'", element)
        time.sleep(3)

    def clickPostFacebook(self):
        button_facebookpost = "//span[@class='_8ung']//button[@role='checkbox']"
        element = self.driver.find_element_by_xpath(button_facebookpost)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",self.driver.find_element_by_xpath("//span[contains(text(),'Post to Facebook')]"))
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,button_facebookpost))
            )
        finally:
            self.driver.execute_script("arguments[0].click();", element)

    def clickScheduleFacebook(self):
        buttonoption = "//span[text()='Post to Facebook']//following-sibling::span/div/button"
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,buttonoption))
            )
        finally:
            element = self.driver.find_element(By.XPATH,buttonoption)
            self.driver.execute_script("arguments[0].click();", element)

    def clickOptionScheduleFacebook(self):
        option_schedule = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//span[contains(text(),'Schedule')]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,option_schedule))
            )
        finally:
            self.driver.find_element(By.XPATH,option_schedule).click()


    def clickScheduleInstagram(self):
        buttonoption = "//button[@class='_271k _271l _1o4e _271m _1qjd']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,buttonoption))
            )
        finally:
            element = self.driver.find_element(By.XPATH,buttonoption)
            self.driver.execute_script("arguments[0].click();", element)

    def clickOptionScheduleInstagram(self):
        option_schedule = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//span[contains(text(),'Schedule')]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,option_schedule))
            )
        finally:
            self.driver.find_element(By.XPATH,option_schedule).click()

    def setSchedule(self,schedule):
        date_instagram = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//div[@class='_gyf']//input[@class='_58al']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,date_instagram))
            )
        finally:
            self.driver.find_element(By.XPATH,date_instagram).click()

        dayschedule = schedule.get("day")
        monthschedule = schedule.get("month")
        "//div[@aria-label='Date picker']"
        getmonthpicker = "//div[@aria-label='Date picker']//h2//span[1]"
        month = self.driver.find_element(By.XPATH,getmonthpicker).text

        conv_month = {
            "January" : 1,
            "February" : 2,
            "March" : 3,
            "April" : 4,
            "May" : 5,
            "June" : 6,
            "July" : 7,
            "August" : 8,
            "September" : 9,
            "October" : 10,
            "November" : 11,
            "December" : 12
            }

        if conv_month.get(month) < conv_month.get(monthschedule):
            nextmonth = "//div[@aria-label='Date picker']//button[span[contains(text(),'Next month')]]"
            self.driver.find_element(By.XPATH,nextmonth).click()
        elif conv_month.get(month) > conv_month.get(monthschedule):
            prevmonth = "//div[@aria-label='Date picker']//button[span[contains(text(),'Previous month')]]"
            self.driver.find_element(By.XPATH,prevmonth).click()
        else:
            pass
        
        self.driver.find_element(By.XPATH,f"//div[@aria-label='Date picker']//div[starts-with(@class,'_owz ')]//span[text()='{dayschedule}']").click()

        time1 = schedule.get("hour")
        input_time1_xpath = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//div[@class='_gyf']//div[span[@aria-label='hours']]/input"
        self.driver.find_element(By.XPATH,input_time1_xpath).send_keys(time1)

        time2 = schedule.get("minute")
        input_time2_xpath = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//div[span[@aria-label='minutes']]/input"
        self.driver.find_element(By.XPATH,input_time2_xpath).send_keys(time2)

        time3 = schedule.get("ampm")
        input_time3_xpath = "//div[contains(@class,'uiContextualLayerPositioner') and not(contains(@class,'hidden_elem'))]//div[span[@aria-label='meridiem']]/input"
        self.driver.find_element(By.XPATH,input_time3_xpath).send_keys(time3)

    def clickSchedule(self):
        element = "//button[@class='_271k _271m _1qjd']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable((By.XPATH,element))
            )
        finally:
            self.driver.find_element(By.XPATH,element).click()

    def getNotificationSuccessfullySchedule(self):
        element = "//span[contains(text(),'Your post has been successfully scheduled.')]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,element))
            )
        finally:
            return True

    def clickCreatePost(self):
        button_createpost_xpath = "//div[contains(text(),'Create Post')]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,button_createpost_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,button_createpost_xpath).click()
            
    def clickCreatePostInstagramFeed(self):
        options_instagramfeed_xpath = "//div[strong[contains(text(),'Instagram Feed')]]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,options_instagramfeed_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,options_instagramfeed_xpath).click()

    def selectInstagramAccount(self,key):
        instagramaccount_xpath = f"//div[contains(text(),'{key}')]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,instagramaccount_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,instagramaccount_xpath).click()

    def clickUser(self):
        user_xpath = "//a[@id='mediaManagerContextSwitcher']"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,user_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,user_xpath).click()

    def clickLogOut(self):
        user_xpath = "//div[div[text()='Log Out']]"
        try:
            WebDriverWait(self.driver,30).until(
                EC.visibility_of_element_located((By.XPATH,user_xpath))
            )
        finally:
            self.driver.find_element(By.XPATH,user_xpath).click() 