from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class addstaff():

    def ASF(self):

        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path= "D:\\Pydrivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseurl)

        driver.find_element_by_id("j_username").send_keys("sudha@hyniva.com")
        time.sleep(2)
        driver.find_element_by_id("j_password").send_keys("urt123")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Staff Details')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[@id='manageStaff']//a[@id='MSF']").click()
        time.sleep(25)
        #driver.find_element_by_partial_link_text("Add Sta").click()
        #driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]").send_keys("\n")
        # to click on No button
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.XPATH, "html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]")).click()
        elem = driver.find_element_by_css_selector("#anchor_595307385")
        important_is_needed = elem.location_once_scrolled_into_view
        elem.click()
        time.sleep(1)
        time.sleep(3)
        driver.find_element_by_xpath("//form[@id='addTeachingStaff']//input[@id='staffName']").send_keys("Kajori")
        time.sleep(3)
        driver.find_element_by_xpath("//form[@id='addTeachingStaff']//input[@id='staffLName']").send_keys("Banerjee")
        time.sleep(3)
        driver.find_element_by_id("//input[@id='gender1']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@id='staffMobileNumber']").send_keys("8495936783")
        time.sleep(3)




SF=addstaff()
SF.ASF()