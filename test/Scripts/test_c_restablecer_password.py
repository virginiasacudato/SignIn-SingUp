from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.RestablecerPassword import RestablecerPassword
import time


class TestRestablecerPassword(WebDriverSetup):

    def test_a_restablecer_pass(self):
        driver = self.driver
        rest_pass = RestablecerPassword(driver)
        rest_pass.login_adm()
        time.sleep(5)
        rest_pass.eth_session()
        rest_pass.volver_emp()
        time.sleep(3)
        rest_pass.eth_gen_pass()
        time.sleep(3)
