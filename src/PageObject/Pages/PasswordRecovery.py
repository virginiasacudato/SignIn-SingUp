from selenium.webdriver.common.by import By
import time


class PasswordRecovery:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        self.password_recovery = '/html/body/main/content/div[4]'
        self.inpt_email = 'Usuario'
        self.btn_recovery = '//*[@id="btnIngresar"]'

    # -- Get Elements --
    def get_password_recovery(self):
        return self.driver.find_element(By.XPATH, self.password_recovery)

    def get_inpt_email(self):
        return self.driver.find_element(By.ID, self.inpt_email)

    def get_btn_recovery(self):
        return self.driver.find_element(By.XPATH, self.btn_recovery)


    # -- Actions --

    def pass_recovery(self):
        self.get_password_recovery().click()
        time.sleep(5)
        with open("base.txt", "r") as file:
            first_line = file.readline()

        self.get_inpt_email().send_keys(str(first_line))
        self.get_btn_recovery().click()
        time.sleep(6)



