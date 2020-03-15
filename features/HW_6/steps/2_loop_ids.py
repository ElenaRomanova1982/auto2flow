from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#locators:
BEST_SELLERS_LINK_LOCATOR = (By.CSS_SELECTOR, "#nav-xshop-container a[href*='bestsellers']")
BESTSELLERS_CATEGORIES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#zg_tabs a")
BESTSELLERS_CATEGORIES_PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")      #***"#zg_banner_text_wrapper" ***"h1#zg_listTitle"



@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')  #ambiguous step

@when('Open Amazon Bestsellers page')
def open_bestsellers_page(context):
    best_sellers_page = context.driver.find_element(*BEST_SELLERS_LINK_LOCATOR)
    best_sellers_page.click()

@then('Verify that every cagetory button will open appropriate page')
def verify_bestsellers_categories(context):
    bestsellers_cagetories_buttons = context.driver.find_elements(*BESTSELLERS_CATEGORIES_BUTTON_LOCATOR)
    for bestsellers_cagetory_button in bestsellers_cagetories_buttons:
        #bestsellers_cagetories_buttons = context.driver.find_elements(*BESTSELLERS_CATEGORIES_BUTTON_LOCATOR)
        bestsellers_cagetory_button.click()
        bestsellers_cagetory_button = context.driver.find_element(*BESTSELLERS_CATEGORIES_BUTTON_LOCATOR)
        category_title = context.driver.find_element(*BESTSELLERS_CATEGORIES_PAGE_TITLE_LOCATOR)
        print(bestsellers_cagetory_button.text)
        print(category_title.text)
        assert bestsellers_cagetory_button.text in category_title.text, f'Expected {bestsellers_cagetory_button.text} to be in {category_title.text}'



'''
get all elements to array, find again and call by index, assert by h1
  *. [Loops] Make a test case which:
Clicks on Best Sellers link on the top menu
Clicks on each top link and verify that new page opens
        '''