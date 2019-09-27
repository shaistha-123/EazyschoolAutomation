import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import unittest


class inactivatestudent(unittest.TestCase):

    def setUp(self):
        print("Running inactivate student")

    def test_methodAC(self):
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
        driver.find_element_by_xpath("//a[@id='viewSub']").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/table[1]/tbody[1]/tr[13]/td[12]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//option[contains(text(),'Inactive')]").click()
        # Selec = Select(driver.find_element_by_xpath("//select[@id='studentStatusId']").click())
        # Selec.select_by_visible_text("Inactive")
        time.sleep(2)
        driver.find_element_by_xpath("//textarea[@id='messageDescription']").send_keys("you are inactivated")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='submitButton1']").click()
        time.sleep(2)

if __name__=='__main__':
    unittest.main(verbosity=2)