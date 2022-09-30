from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import names
import random


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

    # -- Actions --

    def registro_emp(self):
        # Ingresar datos pedidos
        # Cambiar de pestaña a Ethereal
        # Acceder al email fake
        # Ir al email
        # Cambiar a la pestaña dirigida
        # Activar cuenta ¿?
        self.get_signup().click()
        time.sleep(2)
        # Data Random
        self.get_razon_social().send_keys(names.get_first_name())
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
        print(fake_email)
        fake_pass = self.get_fake_pass().text
        print(fake_pass)
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
        time.sleep(5)
        msg_modal = self.get_modal_exitoso().text
        self.get_entendido().click()
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
            print(bandeja_entrada)
            assert False

    def acces_email(self):
        self.get_msg_email().click()
        self.driver.switch_to.frame(self.get_iframe())
        time.sleep(2)
        self.get_link_msg().click()
        time.sleep(5)
