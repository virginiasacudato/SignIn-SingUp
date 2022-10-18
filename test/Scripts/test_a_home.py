from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.Home import Home
import time


class TestHome(WebDriverSetup):

    def test_a_signup_emp(self):
        driver = self.driver
        home = Home(driver)
        home.registro_emp()
        time.sleep(5)
        home.ethereal_fake_identity()
        time.sleep(3)
        home.ingresar_fake_email()
        time.sleep(6)
        home.check_envio_email()
        home.acces_email()
        home.set_pass()
        time.sleep(4)
        home.back_to_login()
        time.sleep(5)

