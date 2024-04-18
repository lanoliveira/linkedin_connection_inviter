from random import uniform

import urllib.parse

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os

import time

load_dotenv(override=True)

email = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# message = ' ,tudo bem?\n\nEstou entrando em contato porque gostaria muito de uma oportunidade para me juntar ao seu time. Sou graduado em Engenharia Civil e estou cursando Engenharia de Computação. Já trabalhei com análise de dados, mineração de informações em diferentes websites, criação de scripts, manipulação de Dashboards em Power BI e tenho habilidades em Python, PySpark, Microsoft Azure e PostgreSQL.\n\n\Poderíamos conversar melhor?\n\nDesde já agradeço pela atenção e fico à disposição.\n\nMuito obrigado,\n\nAlan Araújo'

with open('message.txt', 'r', encoding='utf-8') as file:
    message = file.read()

url = 'https://www.linkedin.com/'

driver = uc.Chrome()

driver.execute_script("window.localStorage.clear();")
driver.execute_script("window.sessionStorage.clear();")
driver.execute_script("window.location.reload();")

driver.get(url)

driver.find_element(By.CSS_SELECTOR, '#session_key').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#session_password').send_keys(password)

driver.find_element(By.CSS_SELECTOR, '.sign-in-form__submit-btn--full-width').click() 

time.sleep(uniform(1.7, 2.2))

driver.get('https://www.linkedin.com/search/results/people/?activelyHiring=%22true%22&geoUrn=%5B%22104746682%22%5D&keywords="engenheiro%20de%20dados"%20OR%20"analista%20de%20dados"%20OR%20"data%20analist"&origin=FACETED_SEARCH&searchId=9444e0da-e1f2-4c31-b717-2eb011b9d618&sid=e2*')

time.sleep(uniform(9.7, 10.3))

invites = 0

while invites < 20:
    try:
        buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Convidar')]")
        invites += len(buttons)

        for button in buttons:
            full_name = button.get_attribute("aria-label").split('Convidar')[1].strip().split(' para')[0].strip()
            name = full_name.split(' ')[0]
            button.click()
            time.sleep(uniform(2.7, 3.2))
            driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Adicionar nota')]").click()
            time.sleep(uniform(2.7, 3.2))
            # driver.find_element(By.CSS_SELECTOR, '#custom-message').send_keys('Olá ' + name.split(' ')[0] + message)
            driver.find_element(By.CSS_SELECTOR, '#custom-message').send_keys(message.replace('[RECRUTADOR]', name))
            time.sleep(uniform(4, 5))
            driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Enviar agora')]").click()
            time.sleep(uniform(2.7, 3.2))
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(uniform(1, 1.3))
    except Exception as e:
        print(e)
        breakpoint()

    driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Avançar')]").click()
    print('Invites sent: ', invites)
    time.sleep(uniform(2.7, 3.2))

driver.quit()