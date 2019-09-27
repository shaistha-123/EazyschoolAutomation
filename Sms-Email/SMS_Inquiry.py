import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import pytest

class SMSInquiry(unittest.TestCase):

    def setUp(self):
        print("Run before every test")

    def test_methodA(self):
        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path="D:\\Pydrivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseurl)

        driver.find_element_by_id("j_username").send_keys("1231231231")
        time.sleep(2)
        driver.find_element_by_id("j_password").send_keys("urt123")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='ASMS']").click()
        time.sleep(4)
        #driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]").click()
        """classname = Select(driver.find_element_by_xpath("//select[@id='className']"))
        classname.select_by_value("140")
        time.sleep(2)
        driver.find_element_by_css_selector("input[value='4652']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input[value='4381']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input[value='3049']").click()
        time.sleep(2)
        #driver.find_element_by_id("selectAllIds").click()
        #time.sleep(2)
        driver.find_element_by_xpath("//textarea[@id='messageDesc']").send_keys("Test SMS",Keys.TAB,Keys.TAB)
        time.sleep(6)
        #driver.find_element_by_xpath("//input[@id='submit_2046265256']").click()
        #driver.find_element_by_class_name("submitBt btn blue").click()
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[7]/div[1]/input[1]").click()
        time.sleep(2)

        #SMSInquiry
        driver.find_element_by_link_text("SMS Inquiry").click()
        time.sleep(2)"""

        #Log out from teacher login

        driver.find_element_by_xpath("//span[@class='username hidden-480']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        time.sleep(2)

        #Login to admin

        driver.find_element_by_id("j_username").send_keys("shanthkumar@hyniva.com")
        time.sleep(2)
        driver.find_element_by_id("j_password").send_keys("shanth123")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='ASMS']").click()
        time.sleep(2)
        driver.find_element_by_link_text("SMS Inquiry").click()
        time.sleep(2)
        if driver.find_element_by_css_selector("#showInquiry").click():
            time.sleep(2)
            print("Inquiry found")
        else:
            print("Inquiry not found")
        driver.find_element_by_xpath("/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]").click()
        time.sleep(2)




if __name__=='__main__':
    unittest.main(verbosity=2)
