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


class chequePayment():

    def chequePay(self):

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
        driver.find_element_by_link_text("Collect Fee").click()
        time.sleep(2)
        driver.find_element_by_xpath("//select[@id='className']").click()
        time.sleep(2)
        time.sleep(2)
        driver.find_element_by_xpath("//select[@id='className']").click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('className'))
        select.select_by_visible_text('II - A')
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[2]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[6]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='clForm']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='partRemainingPayAmt_95_50']").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='partRemainingPayAmt_95_50']").send_keys("10")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='totalPartclrAmt_95_50']").click()
        time.sleep(6)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/form[1]/div[2]/div[1]/div[14]/div[1]/div[1]/input[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[@id='generatChallana']").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/div[1]/input[1]").click()
        time.sleep(2)




CP = chequePayment()
CP.chequePay()
