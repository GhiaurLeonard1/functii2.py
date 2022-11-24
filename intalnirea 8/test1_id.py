# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')


#selector by ID
# chrome.find_element(By.ID, 'first-name').send_keys('TEST ')

try:
    first_name = chrome.find_element(By.ID, 'first-name')#daca adresa id(first-name1) nu este valabila....
    first_name.send_keys('Leonard')#sare peste inlocuire
except Exception as e:#trece las exceptie
    print('ID-ul introdus nu este corect')
print('Am ajuns aici')

sleep(6)
chrome.quit()




