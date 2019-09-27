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


class SendSms():

    def sms(self):

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
        driver.find_element_by_xpath("//span[contains(text(),'SMS / Email')]").click()
        time.sleep(4)
        #driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]").click()
        #time.sleep(2)
        driver.find_element_by_id("msgReceiverType").click()
        time.sleep(2)
        sel2 = Select(driver.find_element_by_xpath("//select[@id='msgReceiverType']"))
        sel2.select_by_value("S")
        time.sleep(2)
        #driver.find_element_by_xpath("//input[@id='mobileNumbers']").send_keys("8495936783")
        #time.sleep(2)
        driver.find_element_by_xpath("//textarea[@id='messageDescriptionDiv']").send_keys("Test Automation SMS")
        time.sleep(2)
        # Send SMS button
        #driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[12]/div[1]/input[1]").click()
        driver.find_element_by_xpath("//input[@id='classWideId']").click()
        time.sleep(2)
        driver.find_element_by_name("chkBoxSelectedAccountIds").click()
        time.sleep(2)
        driver.find_element_by_xpath("//textarea[@id='messageDesc']").send_keys("Automated SMS classwide")
        time.sleep(2)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/form[1]/div[1]/div[7]/div[1]/input[1]").click()
        time.sleep(2)





SS=SendSms()
SS.sms()