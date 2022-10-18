from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import names
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/SignIn-SingUp/.env')
load_dotenv(dotenv_path)

# Environment Variables

PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

random_pass = os.getenv('RANDOM_PASS')


class Home:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        self.body = '/html/body'
        self.signup_emp = '/html/body/main/content/div[5]'
        self.razon_social = 'Nombre'
        self.n_id = 'Cuit'
        self.email = 'Mail'
        # Ethereal
        self.btn_create_account = '//*[@id="create-form"]/div/div/div[2]/h1/button'
        self.fake_email = '/html/body/div[1]/div/div[2]/div/table/tbody/tr[2]/td/code'
        self.fake_pass = '/html/body/div[1]/div/div[2]/div/table/tbody/tr[3]/td/code'
        self.messages = '//*[@id="navbarNav"]/ul[1]/li[4]/a'
        self.gen_pass_msg = '/html/body/div[1]/div/div[3]/div/table/tbody/tr[1]/td[2]/a'
        self.iframe = '//*[@id="message"]/iframe'
        self.link = '/html/body/div[2]/a'
        # Home Page Again
        self.check_terms = 'Terminos'
        self.btn_accept = "//button[@type='button']"
        self.btn_registrar = 'btnIngresar'
        self.modal_text = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[1]/h4'
        self.btn_entendido = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[3]/button'
        self.inpt_pass_emp = '//*[@id="Pass"]'
        self.inpt_repeat_pass = '//*[@id="PassConfirm"]'
        self.activate = '//*[@id="botonLogin"]'
        # Check login
        self.user = 'Usuario'
        self.password = 'Password'
        self.btn_ingresar = 'btnIngresar'
        self.name_corp = '/html/body/main/aside/section/div/div[2]/div/a'

    # -- Get Elements --
    def get_body(self):
        return self.driver.find_element(By.XPATH, self.body)

    def get_signup(self):
        return self.driver.find_element(By.XPATH, self.signup_emp)

    def get_razon_social(self):
        return self.driver.find_element(By.ID, self.razon_social)

    def get_n_id(self):
        return self.driver.find_element(By.ID, self.n_id)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    # Ethereal
    def get_crt_account(self):
        return self.driver.find_element(By.XPATH, self.btn_create_account)

    def get_fake_email(self):
        return self.driver.find_element(By.XPATH, self.fake_email)

    def get_fake_pass(self):
        return self.driver.find_element(By.XPATH, self.fake_pass)

    def get_messages(self):
        return self.driver.find_element(By.XPATH, self.messages)

    def get_iframe(self):
        return self.driver.find_element(By.XPATH, self.iframe)

    def get_link_msg(self):
        return self.driver.find_element(By.XPATH, self.link)

    # Home Page Again
    def get_check_terms(self):
        return self.driver.find_element(By.ID, self.check_terms)

    def get_btn_accept(self):
        return self.driver.find_element(By.XPATH, self.btn_accept)

    def get_btn_registrar(self):
        return self.driver.find_element(By.ID, self.btn_registrar)

    def get_modal_exitoso(self):
        return self.driver.find_element(By.XPATH, self.modal_text)

    def get_entendido(self):
        return self.driver.find_element(By.XPATH, self.btn_entendido)

    def get_msg_email(self):
        return self.driver.find_element(By.XPATH, self.gen_pass_msg)

    def get_inpt_pass(self):
        return self.driver.find_element(By.XPATH, self.inpt_pass_emp)

    def get_repeat_pass(self):
        return self.driver.find_element(By.XPATH, self.inpt_repeat_pass)

    def get_activate(self):
        return self.driver.find_element(By.XPATH, self.activate)

    # Check login
    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingreso(self):
        return self.driver.find_element(By.ID, self.btn_ingresar)

    def get_name_corp(self):
        return self.driver.find_element(By.XPATH, self.name_corp)

    # -- Actions --

    def registro_emp(self):
        # Ingresar datos pedidos
        # Cambiar de pestaña a Ethereal
        # Acceder al email fake
        # Ir al email
        # Cambiar a la pestaña dirigida
        # Activar cuenta
        # def execute_script():
        #    result = self.driver.execute_script('return document.querySelector("#Nombre").value')
        #    value = result.text
        #    return value
        self.get_signup().click()
        time.sleep(2)
        # Data Random
        global random_name
        random_name = names.get_first_name()
        self.get_razon_social().send_keys("MayTest"+random_name)
        # print(execute_script())
        self.get_n_id().send_keys(str(random.randint(20000000000, 30000000000)))

    def ethereal_fake_identity(self):
        global fake_email
        global fake_pass
        link = "https://ethereal.email/"
        self.driver.execute_script("window.open('{}');".format(link))
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        # Create Account
        self.get_crt_account().click()
        time.sleep(1)
        # Save data
        fake_email = self.get_fake_email().text
        #print(fake_email)
        fake_pass = self.get_fake_pass().text
        #print(fake_pass)
        time.sleep(3)
        f = open("base.txt", "w")
        f.write(fake_email + '\n')
        f.write(fake_pass)
        f.close()

    def ingresar_fake_email(self):
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        time.sleep(2)
        self.get_email().send_keys(fake_email)
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Terminos"]'))))
        time.sleep(5)
        self.get_btn_accept().click()
        time.sleep(1)
        self.get_btn_registrar().click()
        time.sleep(10)
        # if msg_modal == 'Operación Exitosa':
        #    assert True
        # else:
        #    print('Test Fallido.')
        #    assert False
        # Check modal existoso

    def check_envio_email(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        self.get_messages().click()
        time.sleep(2)
        bandeja_entrada = self.get_msg_email().text
        if bandeja_entrada == 'Generar Contraseña de empresa':
            assert True
        else:
            #print(bandeja_entrada)
            assert False

    def acces_email(self):
        self.get_msg_email().click()
        self.driver.switch_to.frame(self.get_iframe())
        #print("En el frame!!!!")
        time.sleep(2)
        self.get_link_msg().click()
        time.sleep(5)

    def set_pass(self):
        self.get_inpt_pass().send_keys(random_pass)
        self.get_repeat_pass().send_keys(random_pass)
        self.get_activate().click()

    def back_to_login(self):

        self.get_user().send_keys(fake_email)
        self.get_password().send_keys(random_pass)
        self.get_btn_ingreso().click()
        name_inicio = self.get_name_corp().text
        #print("El nombre del inicio es esto --> ", name_inicio)
        #print("Random name es esto --> ", random_name)
        ref_random_name = "MayTest"+random_name
        if name_inicio == ref_random_name:
            print('Empresa dada de alta correctamente. Test Exitoso.')
            assert True
        else:
            #print('Test Fallido')
            assert False

    # SEGURIDAD PASSWORD
    ## |1 MAYUS
    ## 1 MINUSCULA
    # 1 NUMERO
    # 8 MINIMA
