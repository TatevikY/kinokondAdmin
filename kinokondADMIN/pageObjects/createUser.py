from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:64309/login")
time.sleep(30)

elem = driver.find_element(By.CSS_SELECTOR, 'script."packages/KinoKond/presentation/widgets/form_components/username_input.dart"')
elem.clear()
elem.send_keys("tatevikyyy")
time.sleep(30)



"""
elem = driver.find_element(By.XPATH, "password")
elem.clear()
elem.send_keys("YAyloyan1991%%")

elem = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/form/div[3]/button')
elem.click()
time.sleep(1)
elem = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div[1]/ul/li[4]/a/div[2]/span')
elem.click()

time.sleep(10)
"""
