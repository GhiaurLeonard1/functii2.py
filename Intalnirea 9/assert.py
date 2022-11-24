from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')# deschidem pagina
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()# facem clik pe autocomplete
sleep(1)
actual = chrome.current_url# salvam pagina web actuala intr-o variabila
expected = 'https://formy-project.herokuapp.com/autocomplete'# salvam rezultatul selectorilor in alta variabila
sleep(1)
assert actual == expected, f'Url invalid: expected {expected}, found {actual}'#comparam variabilele daca sunt identice, daca nu ne returneaza eroare
print('Test Passed')


