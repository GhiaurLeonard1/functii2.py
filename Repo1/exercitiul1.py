from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()


chrome.get("https://formy-project.herokuapp.com/ ")


link_test = chrome.find_element(By.LINK_TEXT, 'Autocomplete')
link_test.click()

sleep(3)
chrome.quit()
