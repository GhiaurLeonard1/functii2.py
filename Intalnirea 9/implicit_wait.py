# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# de citit
# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/


s = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=s)

chrome.implicitly_wait(1)#stabilim secundele cat sa caute dupa orice element

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.ID, 'first-name').send_keys('ELON')

chrome.find_element(By.ID, 'last-name').send_keys('MUSK')

chrome.find_element(By.ID, 'job-title').send_keys('INJINER')

sleep(5)    #opreste executia codului daca a gasit toate elementele


