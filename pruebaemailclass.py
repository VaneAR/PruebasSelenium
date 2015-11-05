from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class TestGooglePage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1445013064&rver=6.4.6456.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fbay169.mail.live.com%2Fdefault.aspx%3Frru%3Dinbox&lc=1033&id=64855&mkt=en-us&cbcxt=mai')

    def test_prueba_titulo_de_google(self):
        self.assertEqual('Sign In', self.driver.title)

    def test_acceder_mi_cuenta_hotmail(self):
        user = self.driver.find_element_by_id('i0116')
        passw = self.driver.find_element_by_id('i0118')

        user.send_keys('vane_19940605@hotmail.com')
        passw.send_keys(u'Princesa94')
        passw.send_keys(Keys.RETURN)
        time.sleep(10)
        boton = self.driver.find_element_by_id('ukfbOGy8WD5RG_4AAhWthGpA2')
        boton.click()

        #buscar = cls
    @classmethod
    def teardown(cls):
        cls.driver.close()
if __name__ == '__main__':
    unittest.main()
