from selenium.webdriver.common.by import By
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/SignIn-SingUp/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('URL_TEST')
FAKE_PASS = os.getenv('PASS_FAKE')


class RestablecerPassword:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        # Login
        self.user = 'Usuario'
        self.password = 'Password'
        self.btn_ingresar = 'btnIngresar'
        # Edit Employee
        self.administracion = '/html/body/main/aside/section/nav/ul/li[2]/div/label'
        self.empleados = '/html/body/main/aside/section/nav/ul/li[2]/div/div/ul/li[2]/a'
        self.icon_edit = '//*[@id="btnModificar"]/i'
        self.cloud = '//*[@id="modalNuevoEmpleado"]/div[2]/div/div[2]/div/ul/li[4]/a'
        self.reset_password = '//*[@id="tab_mi_web"]/div/div[1]/button'
        self.confirm = '//*[@id="modal-danger-reset-pass"]/div[2]/div/div[3]/button[2]'
        self.email_emp = '//*[@id="EmailCorp"]'
        # Ethereal
        self.login_eth = '//*[@id="navbarNav"]/ul[2]/li/a'
        self.inpt_email = '//*[@id="address"]'
        self.inpt_pass = '//*[@id="password"]'
        self.btn_login = '/html/body/div[1]/div/div[2]/div/form/div[4]/button'
        self.messages = '//*[@id="navbarNav"]/ul[1]/li[4]/a'
        self.gen_pass_msg = '/html/body/div[1]/div/div[3]/div/table/tbody/tr[1]/td[2]/a'
        self.iframe = '//*[@id="message"]/iframe'
        self.link = '/html/body/div[2]/a'

    # --Get Elements --

    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingresar(self):
        return self.driver.find_element(By.ID, self.btn_ingresar)

    def get_administracion(self):
        return self.driver.find_element(By.XPATH, self.administracion)

    def get_empleados(self):
        return self.driver.find_element(By.XPATH, self.empleados)

    def get_icon_edit(self):
        return self.driver.find_elements(By.XPATH, self.icon_edit)

    def get_cloud(self):
        return self.driver.find_element(By.XPATH, self.cloud)

    def get_reset_password(self):
        return self.driver.find_element(By.XPATH, self.reset_password)

    def get_confirm(self):
        return self.driver.find_element(By.XPATH, self.confirm)

    def get_email_emp(self):
        return self.driver.find_element(By.XPATH, self.email_emp)

    # Ethereal
    def get_ethereal_log(self):
        return self.driver.find_element(By.XPATH, self.login_eth)

    def get_inpt_log(self):
        return self.driver.find_element(By.XPATH, self.inpt_email)

    def get_inpt_pass(self):
        return self.driver.find_element(By.XPATH, self.inpt_pass)

    def get_btn_login(self):
        return self.driver.find_element(By.XPATH, self.btn_login)

    def get_messages(self):
        return self.driver.find_element(By.XPATH, self.messages)

    def get_iframe(self):
        return self.driver.find_element(By.XPATH, self.iframe)

    def get_link_msg(self):
        return self.driver.find_element(By.XPATH, self.link)

    def get_msg_email(self):
        return self.driver.find_element(By.XPATH, self.gen_pass_msg)

    # -- Actions --

    def login_adm(self):
        self.driver.get(BASE_URL)
        self.get_user().send_keys(USER)
        self.get_password().send_keys(PASSWORD)
        self.get_btn_ingresar().click()
        time.sleep(3)
        self.get_administracion().click()
        self.get_empleados().click()
        time.sleep(5)
        edit = self.get_icon_edit()
        edit[1].click()
        time.sleep(2)

    def eth_session(self):
        email_corp = self.get_email_emp().get_attribute('value')
        print(email_corp)
        time.sleep(5)
        link = "https://ethereal.email/"
        self.driver.execute_script("window.open('{}');".format(link))
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        self.get_ethereal_log().click()
        self.get_inpt_log().send_keys(str(email_corp))
        self.get_inpt_pass().send_keys(str(FAKE_PASS))
        self.get_btn_login().click()
        time.sleep(6)

    def volver_emp(self):
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        time.sleep(3)
        self.get_cloud().click()
        self.get_reset_password().click()
        self.get_confirm().click()

    def eth_gen_pass(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        self.get_messages().click()
        time.sleep(2)
        bandeja_entrada = self.get_msg_email()
        bandeja_entrada.click()
        time.sleep(3)


