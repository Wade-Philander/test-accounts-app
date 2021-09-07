from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    def setUp(self):
        # server = "http://127.0.0.1:8000/login/"
        self.browser = webdriver.Chrome('/home/wade/Desktop/work/selenium/chromedriver')
        self.browser.get("http://127.0.0.1:8000/")
        print("browser set up and running")

    def tearDown(self):
        print("browser closed")
        self.browser.close()