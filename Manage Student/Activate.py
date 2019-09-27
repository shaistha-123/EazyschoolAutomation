from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser


class Inactstudent():

    def InS(self):

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
        driver.find_element_by_xpath("//a[@id='MSTI']").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//div[@id='/student/ajaxEnableStudentDetails.do?tempId=4714&tempId1=195&classSectionId=343']").click()
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[8]/div[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[@class='yes']").click()
        time.sleep(2)

INA = Inactstudent()
INA.InS()