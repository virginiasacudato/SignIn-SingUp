from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.PasswordRecovery import PasswordRecovery
import time


class TestRecoveryPassword(WebDriverSetup):

    def test_a_recovery_password(self):
        driver = self.driver
        pass_rec = PasswordRecovery(driver)
        pass_rec.pass_recovery()
