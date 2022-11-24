from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#-initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()


# -----------------------------Selector by Link Text --------------------------------------------------------------------
# #1)
# #navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/')
#
# # folosim selector by link_text
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click() #da clik pe Autocomplete si ne deschide pagina de completare

# #2)
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Buttons').click()

# #3)
# chrome.get("https://the-internet.herokuapp.com/")
# chrome.find_element(By.LINK_TEXT, "Inputs").click()#\\\\\ href="/inputs">Inputs /////

# #4)
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Broken Images').click()

# #5)
# chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Redirect Link').click()

# # 6)
# chrome.get('https://phptravels.net/')
# chrome.find_element(By.LINK_TEXT, 'Blog').click()#\\\\\ href="https://phptravels.net/blog">Blog //////

# #7)
# chrome.get('https://formy-project.herokuapp.com/')
# chrome.find_element(By.LINK_TEXT, 'Checkbox').click()


# -----------------------------Selector by Partial Link Text --------------------------------------------------------------------
# #1)
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Press').click()# o parte din text

# #2)
# chrome.get('https://www.techlistic.com/')
# chrome.find_element(By.PARTIAL_LINK_TEXT, "Choosing Kotlin").click()# din (Why Are Companies Choosing Kotlin For Their App Development) am selectat doar o parte


#-------------------------------------------------Selector by ID---------------------------------------------------------
# #1)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.ID, "street_number").send_keys("10")

# #2)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.ID, "locality").send_keys("Brasov")

# #3)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.ID, 'street_number').send_keys('Aleea Corporatristilor')


# #4)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.ID, 'postal_code').send_keys('245896')

# #5)
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.ID, 'administrative_area_level_1').send_keys('Sectorul Principal')

# #6)
# chrome.get('https://the-internet.herokuapp.com/login')
# chrome.find_element(By.ID, 'username').send_keys('LeoLeutzu')

# # #7)
# chrome.get('https://the-internet.herokuapp.com/login')
# chrome.find_element(By.ID, 'password').send_keys('666')


#---------------------------------------------Selector by Name-------------------------------------------------------------
#1)
# #navigam catre un url
# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, "firstname").send_keys(" Maciupiciu ")

# #2)
# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, "lastname").send_keys(" Madagascar ")

# #3)
# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.NAME, "continents").send_keys(" Africa ")

# #4)
# chrome.get("https://www.phptravels.net/signup")
# chrome.find_element(By.NAME, "phone").send_keys(" 0733456223 ")


#------------------------------------------------Selector by TAG_NAME--------------------------------------------------
# #1)
# chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
# chrome.find_element(By.TAG_NAME, 'input name').send_keys('Orlando')# # #selector by TAG cand e unul singur

##daca gasim mai multe, le punem intr-o lista
# #2)
# chrome.get("https://www.phptravels.net/login")
# input_list = chrome.find_elements(By.TAG_NAME, "input")# tag namer=input or input name
# input_list[0].send_keys("LeoLeutzu@gmail.com")
# input_list[1].send_keys("0000")

# #3)
# chrome.get("https://formy-project.herokuapp.com/form")
# input_list = chrome.find_elements(By.TAG_NAME, "input")
# input_list[0].send_keys("Buna")
# input_list[1].send_keys("eu.Leo")
# input_list[2].send_keys("234")


#---------------------------------------------- Selector by Class Name-------------------------------------------------------------
#1)
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
#
# #daca gasim mai multe, le punem intr-o lista
# input_list = chrome.find_elements(By.CLASS_NAME, "form-control")
# print(input_list)
# input_list[0].send_keys("Eu sunt roman si locuiesc in Romania")
# input_list[1].send_keys("sunt")
# input_list[2].send_keys("roman")
# input_list[3].send_keys("si")
# input_list[4].send_keys("locuiesc")
# input_list[5].send_keys("in")
# input_list[6].send_keys("Romania")


#---------------------------------------------Selector by CSS------------------------------------------------------------
# #dupa ID
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
# chrome.find_element(By.CSS_SELECTOR, "input#autocomplete").send_keys("Leonard")#primul input din autocomplete


# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="City"]').send_keys('Bucuresti')


# #dupa clasa
# chrome.get("https://phptravels.net/signup")
# chrome.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("Ghiaur")

# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input.pac-target-input').send_keys('21')#cand tii mouseul pe linia de comanda din inspect ce contine input, pe pagina iti arata legatura.


# #dupa atribut=valoare partiala
# chrome.get("https://www.phptravels.net/signup")
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Phone"]').send_keys("0722456890")

# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="State"]').send_keys('Romania')



#-----------------------------------------------Selectori by XPATH----------------------------------------------------------------

#3-Atribut valoare

# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//input[@id="autocomplete"]').send_keys('Macarena')
# chrome.find_element(By.XPATH, '//input[@id="street_number"]').send_keys('Nufarului')
# chrome.find_element(By.XPATH, '//input[@id="route"]').send_keys('14')
# chrome.find_element(By.XPATH, '//input[@id="locality"]').send_keys('Cucuietii din deal')
# chrome.find_element(By.XPATH, '//input[@id="postal_code"]').send_keys('631458')

# chrome.get("https://phptravels.net/signup")
# chrome.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('SC')
# chrome.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys('Cucuietii din deal')
# chrome.find_element(By.XPATH, '//input[@type="password"]').send_keys('9999')

#3-dupa textul de pe element ( buton text)

# chrome.get('https://formy-project.herokuapp.com/buttons')
# chrome.find_element(By.XPATH, '//button[text()="Success"]').click()
# chrome.find_element(By.XPATH, '//button[text()="Info"]').click()#butonul text in care este scris textul Info
# chrome.find_element(By.XPATH, '//button[text()="Danger"]').click()

# #1-dupa partial text
# chrome.get('https://formy-project.herokuapp.com')
# chrome.find_element(By.XPATH, '//a[text()="Form"]').click()       # form vine de la href, iar a este numele clasei

# # #1- cu SAU, folosind pipe |
# chrome.get("https://www.phptravels.net/login")
# chrome.find_element(By.XPATH, '//input[@name="email"] | //a[@name="email"]').send_keys("leo007turcu@yahoo.com")
#
# # # 1- cu *
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
# chrome.find_element(By.XPATH, '//*[@id="autocomplete"] ').send_keys("ok")
#


# # #1-in care sa folosesc parent(::)
# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.XPATH, '//label[text="Job title"]/parent::strong')
#
# # #1-in care sa folosesti fratele anterior sau de dupa (la alegere)
# chrome.get("https://formy-project.herokuapp.com/form")
# chrome.find_element(By.XPATH, '//label[text="Job title"]/parent::strong/following-sibling::input').send_keys("QA Automation Tester")


#1-functie ca si cea de la clasa prin care sa poti alege prin parametru cu ce element vrei sa interactionez.
# def select_years_of_experience(select_by_visible_text):
#     years_of_experience_dropdown = Select(chrome.find_element(By.ID, 'select-menu'))
#     years_of_experience_dropdown.select_by_visible_text(select_by_visible_text)
#
# select_years_of_experience("0-1")

sleep(5) #5= numarul de secunde cat sta deschisa pagina dupa ce selectorul si-a facut clik-ul
chrome.quit()
