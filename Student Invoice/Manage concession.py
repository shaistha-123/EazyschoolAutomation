from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ConcessionFee():

    def CF(self):

        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path= "D:\\Pydrivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseurl)

        driver.find_element_by_id("j_username").send_keys("shanthkumar@hyniva.com")
        time.sleep(2)
        driver.find_element_by_id("j_password").send_keys("shanth123")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Student Invoice')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@id='urlDoSchoolFeeConcession']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='col-md-4'] ").click()
        time.sleep(2)

        ele2 = Select(driver.find_element_by_name("className")).select_by_value("141")
        #ele2.select_by_visible_text("II-A")
        time.sleep(2)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]/a[1]").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//input[@id='40F2072F0F1']").clear()
        driver.find_element_by_xpath("//input[@id='40F2072F0F1']").send_keys("100")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='submitButtonMainContent']").click()
        time.sleep(2)
        #driver.find_element_by_id("anchor_1395844327").click()
        #driver.find_element_by_partial_link_text("Back").click()
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/a[1]").click()
        time.sleep(2)


CFF = ConcessionFee()
CFF.CF()