from selenium.webdriver.common.by import By
import random
import names
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/SignIn-SingUp/.env')
load_dotenv(dotenv_path)

# Environment Variables
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('URL')
RANDOM_PASS = os.getenv('RANDOM_PASS')

class PasswordRecovery:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        self.password_recovery = '/html/body/main/content/div[4]'
        self.inpt_email = 'Usuario'
        self.inpt_pass = 'Password'
        self.btn_recovery = '//*[@id="btnIngresar"]'
        # Employee
        self.administracion = '/html/body/main/aside/section/nav/ul/li[2]/div/label'
        self.empleados = '/html/body/main/aside/section/nav/ul/li[2]/div/div/ul/li[2]/a'
        self.btn_add = '//*[@id="Empleados"]/div/div[1]/button'
        self.inpt_name = '//*[@id="Nombre"]'
        self.inpt_surname = '//*[@id="Apellido"]'
        self.dni = '//*[@id="DNI"]'
        self.email_emp = '//*[@id="EmailCorp"]'
        self.save_changes = '//*[@id="modalNuevoEmpleado"]/div[2]/div/div[3]/button[2]'
        # Ethereal
        self.btn_create_account = '//*[@id="create-form"]/div/div/div[2]/h1/button'
        self.fake_email = '/html/body/div[1]/div/div[2]/div/table/tbody/tr[2]/td/code'
        self.messages = '//*[@id="navbarNav"]/ul[1]/li[4]/a'
        self.gen_pass_msg = '/html/body/div[1]/div/div[3]/div/table/tbody/tr[1]/td[2]/a'
        self.iframe = '//*[@id="message"]/iframe'
        self.link = 'a'
        self.inpt_pass_emp = '//*[@id="Pass"]'
        self.inpt_repeat_pass = '//*[@id="PassConfirm"]'
        self.activate = '//*[@id="btnGuardar"]'
        self.fake_pass = '/html/body/div[1]/div/div[2]/div/table/tbody/tr[3]/td/code'
        self.h1_pass = '/html/body/main/section/div[2]/h1'

    # -- Get Elements --
    def get_password_recovery(self):
        return self.driver.find_element(By.XPATH, self.password_recovery)

    def get_inpt_email(self):
        return self.driver.find_element(By.ID, self.inpt_email)

    def get_btn_recovery(self):
        return self.driver.find_element(By.XPATH, self.btn_recovery)

    def get_inpt_pass(self):
        return self.driver.find_element(By.ID, self.inpt_pass)

    def get_administracion(self):
        return self.driver.find_element(By.XPATH, self.administracion)

    def get_mod_empleados(self):
        return self.driver.find_element(By.XPATH, self.empleados)

    def get_btn_add(self):
        return self.driver.find_element(By.XPATH, self.btn_add)

    def get_inpt_name(self):
        return self.driver.find_element(By.XPATH, self.inpt_name)

    def get_inpt_surname(self):
        return self.driver.find_element(By.XPATH, self.inpt_surname)

    def get_dni(self):
        return self.driver.find_element(By.XPATH, self.dni)

    def get_crt_account(self):
        return self.driver.find_element(By.XPATH, self.btn_create_account)

    def get_fake_email(self):
        return self.driver.find_element(By.XPATH, self.fake_email)

    def get_fake_pass(self):
        return self.driver.find_element(By.XPATH, self.fake_pass)

    def get_email_emp(self):
        return self.driver.find_element(By.XPATH, self.email_emp)

    def get_btn_save_changes(self):
        return self.driver.find_element(By.XPATH, self.save_changes)

    def get_messages(self):
        return self.driver.find_element(By.XPATH, self.messages)

    def get_msg_email(self):
        return self.driver.find_element(By.XPATH, self.gen_pass_msg)

    def get_iframe(self):
        return self.driver.find_element(By.XPATH, self.iframe)

    def get_link_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.link)

    def get_pass_employee(self):
        return self.driver.find_element(By.XPATH, self.inpt_pass_emp)

    def get_repeat_pass(self):
        return self.driver.find_element(By.XPATH, self.inpt_repeat_pass)

    def get_activate(self):
        return self.driver.find_element(By.XPATH, self.activate)

    def get_h1_pass(self):
        return self.driver.find_element(By.XPATH, self.h1_pass)

    # -- Actions --
    # Solo para empleados
    # Precondicion --> Tener creado un empleado con un email corporativo asignado
    def change_window(self, num_window):
        window_after = self.driver.window_handles[num_window]
        self.driver.switch_to.window(window_after)

    def employ(self):
        # Desde el portal de administrador > Modulo Empleados > Crear empleado
        # (Acceso a administrador con email de base.txt y password por default)
        # (Acceso a administrador --> Depende de que la empresa este dada de alta)
        # Asignarle un email > Dar de alta password
        # Variable global email
        with open("base.txt", "r") as file:
            first_line = file.readline()

        self.get_inpt_email().send_keys(str(first_line))
        self.get_inpt_pass().send_keys(str(RANDOM_PASS))
        self.get_btn_recovery().click()
        time.sleep(3)
        self.get_administracion().click()
        self.get_mod_empleados().click()
        self.get_btn_add().click()
        time.sleep(5)
        # Data Employee
        self.get_inpt_name().send_keys(names.get_first_name())
        self.get_inpt_surname().send_keys(names.get_last_name())
        self.get_dni().send_keys(str(random.randint(20000000, 40000000)))

    def ethereal_email(self):
        global fake_email
        global fake_password
        link = "https://ethereal.email/"
        self.driver.execute_script("window.open('{}');".format(link))
        self.change_window(1)
        #window_after = self.driver.window_handles[1]
        #self.driver.switch_to.window(window_after)
        time.sleep(2)
        # Create Account
        self.get_crt_account().click()
        time.sleep(1)
        fake_email = self.get_fake_email().text
        fake_password = self.get_fake_pass().text
        #print(fake_email)
        #print(fake_password)

    def ingresar_fake_email_employ(self):
        self.change_window(0)
        #window_before = self.driver.window_handles[0]
        #self.driver.switch_to.window(window_before)
        time.sleep(2)
        self.get_email_emp().send_keys(fake_email)
        self.get_btn_save_changes().click()
        time.sleep(3)

    def alta_employee(self):
        self.change_window(1)
        #window_after = self.driver.window_handles[1]
        #self.driver.switch_to.window(window_after)
        time.sleep(2)
        self.get_messages().click()
        self.get_msg_email().click()
        self.driver.switch_to.frame(self.get_iframe())
        #print("En el frame!!!!")
        self.get_link_msg().click()
        time.sleep(5)
        self.get_pass_employee().send_keys(RANDOM_PASS)
        self.get_repeat_pass().send_keys(RANDOM_PASS)
        self.get_activate().click()
        time.sleep(2)

    def pass_recovery(self):
        self.get_password_recovery().click()
        time.sleep(5)
        self.get_inpt_email().send_keys(fake_email)
        self.get_btn_recovery().click()
        time.sleep(6)

    def back_to_ethereal(self):
        try:
            link = "https://ethereal.email/"
            self.driver.get(link)
            self.get_messages().click()
            self.get_msg_email().click()
            self.driver.switch_to.frame(self.get_iframe())
            self.get_link_msg().click()
            title = self.get_h1_pass().text
            if title == 'Elija una contraseña':
                print("Recuperación de contraseña correctamente realizada. Test exitoso")
                assert True
        except:
            assert False



