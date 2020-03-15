#from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# init driver
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

wait = WebDriverWait(driver, timeout=3)#.untill(some_condition) - explicit wait - specific elements that needs more time

driver.implicitly_wait(5) # - implicit wait

# open the url
driver.get('https://www.google.com/')
driver.wait = WebDriverWait(driver, 10)

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# driver.switch_to_alert().dismiss()



# BTN_SEARCH = (By.XPATH, "//button [@class='Tg7LZd']")
# wait for 4 sec
sleep(4)
driver.find_element(By.XPATH, "//button [@class='Tg7LZd']")
# driver.wait.until(EC.element_to_be_clickable(BTN_SEARCH)).click()



# click search
wait.until('element_to_be_clickable', driver.find_element(By.NAME, 'btnK').click()) #maybe not right - next lesson

driver.find_element(*BTN_SEARCH).click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()