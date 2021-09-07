from django.test.testcases import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class TestLogin(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/Users/allyboy08/Downloads/chromedriver_win32/chromedriver")
        # self.browser.get("https://django-livecrm1.herokuapp.com/")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")
        
    def test_admin_products_page(self):
        
        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)
        
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')
        
        
        submit_btn = self.browser.find_element_by_class_name('login_btn')
        
        
        username_input.send_keys('dennis1')
        password_input.send_keys('bobross21')
        

        submit_btn.click()
        
        self.browser.find_element_by_link_text('Products').click()