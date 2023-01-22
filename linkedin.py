#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from secret import secretEmail, secretPassword

sDict = {
    "url": 'https://www.linkedin.com',

    "login_url": 'https://www.linkedin.com/checkpoint/rm/sign-in-another-account',
    "login_email": 'username',
    "login_password": 'password',
    "value_email": secretEmail ,
    "value_password": secretPassword,

    "onboarding_url": 'https://www.linkedin.com/feed/?trk=onboarding-landing',
    "profile_url": 'https://www.linkedin.com/in/your_username/',
    "dev_url": "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-881884702&keywords=developer&origin=SWITCH_SEARCH_VERTICAL&page=3&position=0&searchId=49908181-d8a7-43d3-9723-ac5e9a9c3570&sid=9TU",
    "dev_url_begin": "https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-881884702&keywords=developer&origin=SWITCH_SEARCH_VERTICAL&page=",
    "dev_url_end": "&position=0&searchId=49908181-d8a7-43d3-9723-ac5e9a9c3570&sid=9TU"
}

print("BEGIN driver developers")
driver = webdriver.Chrome()
print("END driver developers")

# Open the LinkedIn login page
driver.get(sDict["login_url"])
driver.implicitly_wait(5)

# Find the email field and enter your email address
print("BEGIN email_input developers")
email_input = driver.find_element(by=By.ID, value=sDict["login_email"])
email_input.send_keys(sDict["value_email"])
print("END email_input developers")
# Find the password field and enter your password
print("BEGIN password_input developers")
password_input = driver.find_element(by=By.ID, value=sDict["login_password"])
password_input.send_keys(sDict["value_password"] + Keys.RETURN)
print("END password_input developers")

# Wait for the page to load
wait = WebDriverWait(driver, 10)

print("BEGIN search_button developers")
search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-global-typeahead__collapsed-search-button")))
search_button.click()
print("END search_button developers")

wait = WebDriverWait(driver, 5)
print("BEGIN search_input developers")
search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
search_input.send_keys("developer" + Keys.RETURN)
print("END search_input developers")

wait = WebDriverWait(driver, 5)

for i in range(1, 10):
    driver.get(sDict["dev_url_begin"] + str(i) + sDict["dev_url_end"])

    wait = WebDriverWait(driver, 20)
    print("BEGIN search_result developers")

    li_elements = driver.find_elements(by=By.CLASS_NAME, value='reusable-search__result-container')

    #iterate through each elements
    for li_element in li_elements:
        print(li_element.text)

driver.quit()