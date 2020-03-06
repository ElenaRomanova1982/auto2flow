from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# init driver
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

# driver.implicitly_wait(4)

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
driver.find_element(*BTN_SEARCH).click()

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()