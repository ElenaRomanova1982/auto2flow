from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

HELP_BUTTON = (By.XPATH, "//a[contains(text(), 'Help')]")
HELP_SEARCH = (By.XPATH, "//input[@id='helpsearch']")
QUESTION = "Cancel order"
SOLUTION = "Cancel Items or Orders"

HELP_SEARCH_GO = (By.XPATH, "//input[@class='a-button-input']")
HELP_CONTENT = (By.XPATH, "//div[@class='help-content']")

driver.get('https://www.amazon.com/')
driver.find_element(*HELP_BUTTON).click()
find_solution =  driver.find_element(*HELP_SEARCH)
find_solution.clear()
find_solution.send_keys(QUESTION)

sleep(5)

driver.find_element(*HELP_SEARCH_GO).click()

assert SOLUTION in driver.find_element(*HELP_CONTENT).text
#assert 'cancel' in driver.current_url           #find_element(By.XPATH, "//div[@class='g']").text

driver.quit()