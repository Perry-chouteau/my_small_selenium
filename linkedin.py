#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from secret import secretEmail, secretPassword
# DEPRECATED
#webdriver = {
#    "Firefox": webdriver.Firefox(executable_path='./geckodriver'),
#    "Chrome" : webdriver.Chrome(executable_path='./chromedriver')
#}


sDict = {
    "url": 'https://www.linkedin.com',

    "login_url": 'https://www.linkedin.com/checkpoint/rm/sign-in-another-account',
    "login_email": 'username',
    "login_password": 'password',
    "value_email": secretEmail ,
    "value_password": secretPassword,

    "onboarding_url": 'https://www.linkedin.com/feed/?trk=onboarding-landing',
    "profile_url": 'https://www.linkedin.com/in/your_username/'
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
#print("BEGIN more_result_button developers")
#more_result_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app-aware-link")))
#more_result_button.click()

driver.get("https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-881884702&keywords=developer&origin=SWITCH_SEARCH_VERTICAL&position=0&searchId=49908181-d8a7-43d3-9723-ac5e9a9c3570&sid=1gZ")

#person_result_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button\
#     search-reusables__filter-pill-button")))
#person_result_button.click()
#print("END more_result_button developers")

wait = WebDriverWait(driver, 20)
print("BEGIN search_result developers")
#search_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "reusable-search__entity-result-list")))
#li_element = wait.until(EC.presence_of_element_located(By.CLASS_NAME, "reusable-search__entity-result-list"))
#li_elements = driver.find_elements_by_class_name("reusable-search__result-container")

li_elements = driver.find_elements(by=By.CLASS_NAME, value='reusable-search__result-container')

#iterate through each elements
for li_element in li_elements:
    print(li_element.text)

print("END search_result developers")

print("BEGIN img_result developers")
#imgs = driver.find_elements(by=By.CLASS_NAME, value='app-aware-link  scale-down')
#
#for img in imgs:
#    print(img.text)
#print("END img_result developers")

#li_elements = driver.find_elements_by_xpath('//ul[@class="reusable-search__entity-result-list"]/li')

#for li in li_elements:
#    print(li.text)

# Wait for the page to load

# Navigate to your profile page
#driver.get(sel_dict["onboarding_url"])

driver.quit()

