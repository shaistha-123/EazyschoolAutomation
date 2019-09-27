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


class SendEmail():

    def Email(self):

        baseurl = "http://dev.eazyschool.in"
        driver = webdriver.Firefox(executable_path= "D:\\Pydrivers\\geckodriver.exe")
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
        driver.find_element_by_link_text("Send Email").click()
        time.sleep(2)
        dropdown2 = Select(driver.find_element_by_id("msgReceiverType"))
        dropdown2.select_by_value("O")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='email']").send_keys("shaistha@hyniva.com,sudha@hyniva.com,madhu@hyniva.com")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='title']").send_keys("Automation Mail")
        time.sleep(5)
        ele4 = driver.find_element_by_xpath("//div[@id='messageContDiv']//iframe[@class='wysihtml5-sandbox']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='messageContDiv']//iframe[@class='wysihtml5-sandbox']").send_keys("Testing automation emails",Keys.TAB,Keys.TAB)
        time.sleep(5)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/form[1]/div[10]/div[1]/input[1]").click()
        time.sleep(2)

        #driver.find_element_by_css_selector("#submit_2001241609").click()
        """try:

            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "submit_2001241609"))
            )
        finally:
                driver.quit()"""

SE = SendEmail()
SE.Email()