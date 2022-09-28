import unittest
from selenium import webdriver
import urllib3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/SignIn-SingUp/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('URL')


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        p = {'download.default_directory': r"C:\Users\Maynar\Desktop\Test-Files"}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('prefs', p)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

