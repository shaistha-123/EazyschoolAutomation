import pytest
import unittest
from selenium import webdriver
import time

@pytest.yield_fixture()
def setUp():
    print("Run this before")
    baseurl = "http://dev.eazyschool.in"
    driver = webdriver.Firefox(executable_path="D:\\Pydrivers\\geckodriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(baseurl)
    yield
    print("Run this after")

def test_methodA(setUp):
    driver = webdriver.Firefox(executable_path="D:\\Pydrivers\\geckodriver.exe")
    print("Run method A")
    driver.find_element_by_id("j_username").send_keys("sudha@hyniva.com")
    time.sleep(2)
    driver.find_element_by_id("j_password").send_keys("urt123")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='btn btn-success uppercase']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='MSTI']").click()
    time.sleep(1)

def test_methodB(setUp):
    print("Run method B")



