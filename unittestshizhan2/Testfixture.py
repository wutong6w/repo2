import unittest
from selenium import webdriver
import time
class Testjiaju(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        time.sleep(2)
        self.driver.get('http://192.168.200.172:8097/html/login.html?returnUrl=http://192.168.200.172:8098/html/index.html')

    def tearDown(self) -> None:
        self.driver.quit()