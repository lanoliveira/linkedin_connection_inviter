from random import uniform
import urllib.parse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import undetected_chromedriver as uc
import time

load_dotenv(override=True)

keywords = 'engenheiro de dados OR analista de dados OR data analist OR dados'
keywords = urllib.parse.quote(keywords)

email = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

with open('message.txt', 'r', encoding='utf-8') as file:
    message = file.read()

url = 'https://www.linkedin.com/'

driver = uc.Chrome()

driver.get(url)

driver.find_element(By.CSS_SELECTOR, '#session_key').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#session_password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '.sign-in-form__submit-btn--full-width').click()

wait = WebDriverWait(driver, 10)

# Wait for the search bar to appear after login
search_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-global-typeahead__input')))
search_bar.clear()
search_bar.send_keys(Keys.RETURN)  # This sends the RETURN key to dismiss the suggestion box

search_url = f'https://www.linkedin.com/search/results/people/?activelyHiring=%22true%22&geoUrn=%5B%22105871508%22%5D&keywords={keywords}&origin=FACETED_SEARCH&sid=E%3BT'
driver.get(search_url)

invites = 0
while invites < 20:
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@aria-label, 'Convidar')]")))
        for button in buttons:
            full_name = button.get_attribute("aria-label").split('Convidar')[1].strip().split(' para')[0].strip()
            name = full_name.split(' ')[0]
            button.click()
            note_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Adicionar nota')]")))
            note_button.click()
            custom_message = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#custom-message')))
            custom_message.send_keys(message.replace('[RECRUTADOR]', name))
            send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Enviar agora')]")))
            send_button.click()
            invites += 1
            time.sleep(uniform(2.7, 3.2))
    except Exception as e:
        print(e)

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Avançar')]")))
    next_button.click()
    print('Invites sent: ', invites)

driver.quit()
