from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

TOOLTIP_LOCATOR = (By.CSS_SELECTOR, "#nav-signin-tooltip") #".nav-signin-tt.nav-flyout"

#@given('Open Amazon main page')   - ambiguous step
#def open_main_page(context):
    #context.driver.get('https://www.amazon.com/')

@when('Sign in tooltip is clickable')
def wait_signin_tooltip_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(TOOLTIP_LOCATOR))

@when('Sign in tooltip will hide')
def wait_signing_tooltip_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element(TOOLTIP_LOCATOR))

@then('Tooltip is not clickable')
def wait_tooltip_not_clickable(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(TOOLTIP_LOCATOR))
