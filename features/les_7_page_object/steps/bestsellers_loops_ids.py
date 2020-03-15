from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#locators:

TOP_LINKS_LOCATOR = (By.CSS_SELECTOR, "#zg_tabs a")
HEADER_LOCATOR = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")



@given('Open Bestsellers page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
     top_links = context.driver.find_elements(*TOP_LINKS_LOCATOR)
     for x in range(len(top_links)):
         link_to_click = context.driver.find_elements(*TOP_LINKS_LOCATOR)[x]
         print(f'\n{x} link =', link_to_click)
         link_text = link_to_click.text

         link_to_click.click()
         sleep(3)

         next_text = context.driver.find_element(*HEADER_LOCATOR).text
         assert link_text in next_text, f'Expected {link_text} to be in {next_text}'
         print(link_text)
         print(next_text)