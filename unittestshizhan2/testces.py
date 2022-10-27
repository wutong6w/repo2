from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from Testfixture import Testjiaju

class Test(Testjiaju):

    def test01_login(self):
        self.driver.find_element_by_id('u9_input').send_keys('wutong6')
        self.driver.find_element_by_id('u14_input').send_keys('123456')
        self.driver.find_element_by_css_selector('#u2_text > p').click()
        chenggong= self.driver.find_element_by_id('loginUser')
        jieguo=chenggong
        chenggong=self.driver.find_element_by_id('loginUser')
        #断言
        self.assertEqual(chenggong,jieguo)

    def test02_login(self):
        self.driver.find_element_by_id('u9_input').send_keys('wutong7')
        self.driver.find_element_by_id('u14_input').send_keys('123456')
        self.driver.find_element_by_css_selector('#u2_text > p').click()
        chenggong= self.driver.find_element_by_id('errorInfo')
        jieguo=chenggong
        chenggong=self.driver.find_element_by_id('errorInfo')
        #断言
        self.assertEqual(chenggong,jieguo)
    def test03_login(self):
        self.driver.find_element_by_id('u9_input').send_keys('wutong6')
        self.driver.find_element_by_id('u14_input').send_keys('1234567')
        self.driver.find_element_by_css_selector('#u2_text > p').click()
        chenggong= self.driver.find_element_by_id('errorInfo')
        jieguo=chenggong
        chenggong=self.driver.find_element_by_id('errorInfo')
        #断言
        self.assertEqual(chenggong,jieguo)



















