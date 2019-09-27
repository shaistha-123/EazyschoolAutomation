import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import pytest

class studentcase(unittest.TestCase):

    def setUp(self):
        print("Run before every test")

    def test_methodA(self):
        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path="D:\\Pydrivers\\geckodriver.exe")
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
        time.sleep(1)
        driver.find_element_by_xpath("//a[@id='addStudentSetting']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//select[@id='studyClassId']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//option[contains(text(),'PRIMARY - A')]").click()
        time.sleep(2)
        # driver.find_element_by_xpath("//input[@id='as-input-032']").send_keys("PA-100")
        driver.find_element_by_name("userVo.admissionNumber").send_keys("PA-226")
        time.sleep(2)
        driver.find_element_by_id("driverfName").send_keys("Sha")
        time.sleep(1)
        driver.find_element_by_id("categoryId").click()
        driver.find_element_by_xpath("//option[contains(text(),'General')]").click()
        time.sleep(1)
        driver.find_element_by_id("fatherName").send_keys("Fname1")
        time.sleep(2)
        driver.find_element_by_id("stumobileNumber").send_keys("1234567890")
        time.sleep(2)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[41]/div[1]/input[1]").click()
        time.sleep(1)
        driver.find_element_by_id("nationality").send_keys("Indian")
        time.sleep(2)
        # driver.find_element_by_id("submit_1326646977").click()
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[12]/div[1]/div[1]/input[1]").click()
        # driver.find_element_by_id("anchor_1626185855").click()
        # driver.find_element_by_partial_link_text("javascript:void(0)").click()
        # driver.find_element_by_class_name("fa fa-edit").click()
        time.sleep(2)
        # driver.find_element_by_xpath("//a[@id='urlClassAssignment']").click()

        # --------Edit Student code--------------
        """driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[10]/a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@id='motherName']").send_keys("Mname")
        time.sleep(2)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[41]/div[1]/input[1]").click()
        # driver.find_element_by_css_selector("#submit_1080198232").click()
        time.sleep(2)
        driver.find_element_by_partial_link_text("Canc").click()
        time.sleep(2)"""

if __name__=='__main__':
    unittest.main(verbosity=2)