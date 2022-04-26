from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

bot_id = "5109024662:AAHKCkKFmSxBMA_ay4sJhz3Y07AL3j3lxzU"
chat_id = "-619212012"
base_url = "https://api.telegram.org/bot" + bot_id + "/sendMessage?chat_id=" + chat_id + '&text=Ledig time funnet'

driver.get("https://www.vegvesen.no/dinside/dittforerkort/timebestilling/timer#/endre/sak/848542648/klasse/A2/trafikkstasjonId/031")


time.sleep(60)
def finnTid():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

found_time = False
counter = 0

while not found_time:
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div/div/div/div[2]')
    except NoSuchElementException:
        time.sleep(random.randint(50, 90))
        driver.refresh()
        time.sleep(10)
        counter = counter + 1
        print("Siden har blitt refreshet {antall} ganger. Kl {tid} ".format(antall=counter, tid = finnTid())) 
    else: 
        requests.get(base_url)
        found_time = True
        