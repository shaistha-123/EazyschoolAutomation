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


class SanityCheck():

    def Sanity(self):

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
        driver.find_element_by_xpath("//div[@id='adminAttendanceDiv']//div[@class='visual']").click()
        time.sleep(2)
        #driver.execute_script("window.history.go(-1)")
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='sendSms']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='invoiceDiv']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='exminationDiv']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='assginmentDiv']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='studentInfo']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='staffInfo']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='manageLeaves']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='IdCardGeneration']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='admissionsDiv']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='reportsDiv']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='help']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'Dashboard')]").click()
        time.sleep(2)








SC = SanityCheck()
SC.Sanity()
