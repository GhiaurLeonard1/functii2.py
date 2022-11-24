import unittest
from time import sleep
from unittest import TestCase

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(TestCase):
    LOGIN_BTN = (By.XPATH, '//a[text()="Form Authentication"]')
    MESSAGE_ERROR_LOGIN = (By.XPATH, '//div//div//div[@class= "flash error"]')
    MESSAGE_SUCCES_LOGIN = (By.XPATH, '//div[@id="flash"]')
    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.implicitly_wait(2)
        self.chrome.find_element(*self.LOGIN_BTN).click()


    def tearDown(self) -> None:
        self.chrome.quit()

    def test1(self):#verificam ca noul url este corect
        actual = self.chrome.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual, expected, "The page is correct")

    def test2(self):#verificam ca titlul paginii este corect
        actual = self.chrome.title
        expected = "The Internet"
        self.assertEqual(actual, expected, "The Title is correct")

    def test3(self):#verificam ca textul de pe element este corect
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        expected = "Login Page"
        self.assertEqual(actual, expected)

    def test4(self):# verificam ca butonul de login este corect
        self.chrome.find_element(By.XPATH, '//form/button').is_displayed()


    def test5(self):#Verificam ca atributul href al linkului"Elemental Selenium" este corect
        self.chrome.find_element(By.XPATH, '//a[text()="Elemental Selenium"]').is_enabled()

    def test6(self):#Lasam goale user si pass, dam clik pe login, verificam ca eroarea este displayed
        self.chrome.find_element(By.XPATH, '//form/button').click()
        message = self.chrome.find_element(*self.MESSAGE_ERROR_LOGIN)#am salvat eroarea intr-o variabila
        self.assertTrue(message.is_displayed(), "The message is correct")

    def test7(self):#completam cu usser si pass invalide, dam clik pe login, verificam ca mesajul de pe eroare este corect,
        self.chrome.find_element(By.XPATH, '//input[@id = "username"]').send_keys('invalid')
        self.chrome.find_element(By.XPATH, '//input[@id = "password"]').send_keys('invalid')
        self.chrome.find_element(By.XPATH, '//form/button').click()
        actual = self.chrome.find_element(By.XPATH, '//div//div//div[@class= "flash error"]').text
        expected = 'You username is invalid'
        self.assertFalse(actual in expected, "Error message text is incorrect")

    def test8(self,):#lasam casutele goale si apasam login, apoi apasam x la eroare, apoi verificam ca nu mai apare eroarea
        self.chrome.find_element(By.XPATH, '//form/button').click()
        self.chrome.find_element(By.XPATH, '//a[@class = "close"]').click()
        actual = WebDriverWait(self.chrome, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//div//div//div[@class="flash error"]'),
                                                      "Your username is invalid!"))
        if actual:
            print("Message is not displayed")
        else:
            print("Message is displayed")

    def test9(self):#Ia ca o lista toate //label,Verificam textul ca textul de pe ele sa fie cel asteptat (Username si Password),vom avea 2 asserturi
        actual = [self.chrome.find_element(By.XPATH, '//label[@for="username"]').text, self.chrome.find_element(By.XPATH, '//label[@for="password"]').text]
        expected = ["Username", "Password"]
        self.assertEqual(actual[0], expected[0]) and self.assertEqual(actual[1], expected[1])


    def test10(self):#Completam cu user si pass valide,,
        self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//form/button').click()#Click login
        WebDriverWait(self.chrome, 5).util(EC.presence_of_element_located((By.XPATH, '//div//div//div[@class="flash success"]')))#Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
        actual = self.chrome.current_url
        expected ='https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual, expected, "The page is not open correct")#,Verifica ca noul url CONTINE /secure
        message2 = self.chrome.find_element(*self.MESSAGE_SUCCES_LOGIN)
        self.assertTrue(message2.is_displayed(), "The page is not correct")#,Verifica ca elementul cu clasa=’flash succes’ este displayed
        actual = self.chrome.find_element(By.XPATH, '//div[@id="flash"]').text
        expected = "secure area!"
        self.assertTrue(expected in actual, "The message is correct")#,Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’

    def test11(self):#Completeaza cu user si pass valide,Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
        self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//form/button').click()  # Click login
        self.chrome.find_element(By.XPATH, '//div//a[@class= "button secondary radius"]').click()  # Click logout
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, "The page is not open correct")


    def test12(self):# #brute force password hacking
        text_of_website = self.chrome.find_element(By.XPATH, '//div/h4').text
        x = text_of_website.split()
        for split in x:
            self.chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
            self.chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys(split)
            self.chrome.find_element(By.XPATH, '//form/button').click()
            if self.chrome.current_url == 'https://the-internet.herokuapp.com/secure':
                print(f"The secret password is {split}")
                break
        else:
            print("I couldn't find the password")


