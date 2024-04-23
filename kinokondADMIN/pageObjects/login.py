from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

elm_username = "input[id='username']"
elm_password = "input[type='password']"
elm_login = "span[class='p-button-label']"

val_url = "http://localhost:4200/"
val_username = "tatevikyyy"
val_password = "Test123!"

driver = webdriver.Chrome()
driver.get(val_url)
time.sleep(5)

elem = driver.find_element(By.CSS_SELECTOR, elm_username)
elem.clear()
elem.send_keys(val_username)
time.sleep(2)

elem = driver.find_element(By.CSS_SELECTOR, elm_password)
elem.clear()
elem.send_keys(val_password)
time.sleep(2)

elem = driver.find_element(By.CSS_SELECTOR, elm_login)
elem.click()
