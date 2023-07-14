from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests



dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com')
time.sleep(10)

def bot():

    try:
        bolinha = driver.find_element(By.CLASS_NAME,'aumms1qt')
        bolinha = driver.find_elements(By.CLASS_NAME,'aumms1qt')
        click_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.actions_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(click_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
    
    except:
        print('buscando novas notificações')

while True:
    bot()