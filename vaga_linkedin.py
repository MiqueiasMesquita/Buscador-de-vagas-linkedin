from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome("chromedriver.exe")

navegador.get("https://www.linkedin.com/login")

input_email = navegador.find_element_by_id("username")
input_email.send_keys('xxxxxxxxx')

input_senha = navegador.find_element_by_id("password")
input_senha.send_keys('xxxxxxxx')

btn_login = navegador.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

busca = navegador.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys("Python")
busca.send_keys(Keys.RETURN)

time.sleep(3)

filtro_vagas = navegador.find_element_by_xpath("//button[@aria-label='Vagas']")

input('')


