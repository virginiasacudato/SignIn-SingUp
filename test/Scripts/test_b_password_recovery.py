from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.PasswordRecovery import PasswordRecovery
import time


#class TestRecoveryPassword(WebDriverSetup):
#
### SOLAMENTE PARA EMPLEADOS
#    def test_a_recovery_password(self):
#        driver = self.driver
#        pass_rec = PasswordRecovery(driver)
#        pass_rec.employ()
#        time.sleep(3)
#        pass_rec.ethereal_email()
#        time.sleep(3)
#        pass_rec.ingresar_fake_email_employ()
#        time.sleep(4)
#        pass_rec.alta_employee()
#        time.sleep(3)
#        pass_rec.pass_recovery()
#        pass_rec.back_to_ethereal()