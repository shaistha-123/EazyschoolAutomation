from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
from selenium.webdriver.support.ui import Select
import pytest


class Sendcreds(unittest.TestCase):


    def setUp(self):

        print("Run before every test")

    def test_methodA(self):

        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path="D:\\Pydrivers\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(baseurl)

        driver.find_element_by_id("j_username").send_keys("shanthkumar@hyniva.com")
        time.sleep(2)
        driver.find_element_by_id("j_password").send_keys("shanth123")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(),'SMS / Email')]").click()
        time.sleep(4)
        #driver.find_element_by_link_text("Send Email").click()
        #time.sleep(2)
        driver.find_element_by_partial_link_text("Send Login Credentia").click()
        time.sleep(2)
        driver.find_element_by_xpath("//select[@id='msgReceiverType']")
        time.sleep(2)
        sel2= Select(driver.find_element_by_id("msgReceiverType"))
        sel2.select_by_value("P")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='chkBoxSelectedAccountIds-1']").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//input[@id='submit_655752899']").click()

        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[11]/div[1]/input[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("")


if __name__=='__main__':
    unittest.main(verbosity=2)




