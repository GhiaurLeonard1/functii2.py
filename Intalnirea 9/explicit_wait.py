# pip install selenium
# pip install webdriver-manager

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=s)

chrome.implicitly_wait(5)# asteapta cate 2 sec pentru fiecare send keys sa il completeze

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.ID, 'first-name').send_keys('ELON')

#EC= Expected Conditions
chrome.find_element(By.ID, 'last-name').send_keys('MUSK')
job_title = WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.ID, "job-title")))#stabilim cate secunde sa caute dupa un elemnt particular
job_title.send_keys('INJINER_TEST')

sleep(5)#opreste executia codului doar daca a gasit si afisat elementele, altfel asteapta secundele explitit wait si da eroare

