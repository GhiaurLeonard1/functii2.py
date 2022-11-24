import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
class FirefoxOpen(unittest.TestCase):
    def setUp(self):
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        s = Service(GeckoDriverManager().install())
        self.firefox = webdriver.Firefox(service=s)
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(4)
        self.firefox.get('https://formy-project.herokuapp.com/form')

    def tearDown(self):
        self.firefox.quit()

    def test_browser_firefoxOpen(self):
        self.firefox.find_element(By.ID, 'first-name').send_keys('Matei')


        sleep(3)


'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''


