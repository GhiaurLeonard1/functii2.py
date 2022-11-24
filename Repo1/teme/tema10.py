import unittest
import HtmlTestRunner
from unittest import TestSuite
from unittest import TestCase
from Repo1.teme.tema9 import Login
from Intalnirea10.test_alerts import Alerts
from Intalnirea10.test_auth import Authentication
from Intalnirea10.test_context_menu import ContextMenu
from Intalnirea10.test_keys import Keyboard
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)

        ])
        runner = HtmlTestRunner.HTMLTestRunner \
                (
                combine_reports=True,
                report_title='TestReport1',
                report_name='Nume Rezultat Teste 24.11.2022'
            )

        runner.run(teste_de_rulat)

#Ran 20 tests in 0:03:42, OK   ,  Generating HTML reports... ,  reports\Nume Rezultat Teste 24.11.2022_2022-11-24_11-26-06.html



