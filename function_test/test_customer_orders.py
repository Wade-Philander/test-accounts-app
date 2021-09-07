from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from accounts.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from base_test import BaseTest

class TestOrders(StaticLiveServerTestCase):
    def setUp(self):
        #  server = "http://127.0.0.1:8000/"
         self.browser = webdriver.Chrome('/home/wade/Desktop/work/selenium/chromedriver')
         self.browser.get("http://127.0.0.1:8000/")

    def tearDown(self):
         self.browser.close()

    def  test_customer_views_and_place_order_query(self):
         self.browser.get(self.live_server_url)


    def test_update_order(self):
        # driver = self.driver

        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("")
            self.password = self.browser.find_element_by_name("password")
            self.password.send_keys("")
            self.signbtn = self.browser.find_element_by_class_name("btn")
            self.signbtn.click()
            time.sleep(5120)

        except Exception as err:
            print(err)

        try:
            # allOrders = (self.browser.find_element_by_id("btn-sm"))
            self.update = self.browser.find_elements_by_link_text('Update')
            print(self.update)
            self.update.click()


        except Exception as err:
            print(err)
            self.browser.quit

            # driver.get(self.base_url)

        try:
            self.statChange = self.browser.find_element_by_id("id_status")
            print(self.statChange)
            self.statChange.click()

            self.change = self.browser.find_element_by_id("id_status")
            

        except Exception as err:
            self.browser.quit
