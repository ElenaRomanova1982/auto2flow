from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

ORDERS = (By.XPATH, "//a[@id='nav-orders']")
SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")


driver.get('https://www.amazon.com/')

driver.find_element(*ORDERS).click()
sleep(4)

assert "Sign-In" in driver.find_element(*SIGN_IN).text

driver.quit()