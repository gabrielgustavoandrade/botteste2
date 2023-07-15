from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + dir_path + "/profile/zap")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com')
time.sleep(10)

def bot():
    try:
        bolinha = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
        click_bolinha = bolinha[-1]
        
        action = ActionChains(driver)
        action.move_to_element_with_offset(click_bolinha, 0, -20)
        action.click().perform()
        action.click().perform()
    
    except IndexError:
        print('No new notifications found')
    
    except Exception as e:
        print('An error occurred:', str(e))

while True:
    bot()
