import unittest
from selenium import webdriver
import urllib3
import os
from selenium.webdriver.common.by import By
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/LegajoDigital/.env')
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
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        # Login
        self.driver.find_element(By.ID, 'Usuario').send_keys(USER)
        self.driver.find_element(By.ID, 'Password').send_keys(PASSWORD)
        self.driver.find_element(By.ID, 'btnIngresar').click()