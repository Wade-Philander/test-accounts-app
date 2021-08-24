from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from accounts.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

# driver = webdriver.Chrome("/home/wade/Desktop/work/selenium/chromedriver")

# driver.get("http://127.0.0.1:8000/login/")

class TestCMRApp(StaticLiveServerTestCase):
    def setUp(self):
        # server = "http://127.0.0.1:8000/login/"
        self.browser = webdriver.Chrome('/home/wade/Desktop/work/selenium/chromedriver')
        self.browser.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.browser.close()

    # TEST LOGIN FORM 
    #zxcvgbhjkllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

    def TestIfCustomerExist(self):
        self.browser.get(self.live_server_url)
        #time.sleep(120)
        
        # User requests the page for the first time 

        form = self.browser.find_element_by_class_name('form-control')
        self.assertEquals(
            form.find_element_by_class_name('login_btn').text,
            'Login successfully'
        )

    def TestCustomerLoginForm(self):
        # username = self.browser.find_element_by_name('username')
        self.username = WebDriver(self.browser.find_element_by_name('username'))
        
        print("username working")

        self.password = WebDriver(self.browser.find_element_by_name('password'))
        print("pass working")

        submit = WebDriver(self.browser.find_element_by_class_name('login_btn'))
        submit.click()
        print("clicking")

    def TestCustomerRegisterForm(self):
        self.username = WebDriver(self.browser.find_element_by_id('id_username'))
        
        self.email = WebDriver(self.browser.find_element_by_id('id_password1'))
        