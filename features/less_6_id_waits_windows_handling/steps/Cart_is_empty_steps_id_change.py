from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# locators:
CART_BUTTON = (By.ID, "nav-cart")
CART_HEADER = (By.CSS_SELECTOR, "h1")

# other constants:
CART_HEADER_EXPECTED = "Cart is empty"

@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart icon')
def click_on_cart_icon(context):
    cart_icon = context.driver.find_element(*CART_BUTTON)
    print(cart_icon)
    context.driver.refresh()  #selenium-webdriver-browser_manipulation
    sleep(2)
    cart_icon_2 = context.driver.find_element(*CART_BUTTON)
    print(cart_icon_2)
    cart_icon_2.click()
    sleep(2)
    #google_chrome_inspect-network DOMconnect vnizu



@then('{cart_header_content} displayed in Cart Page header')
def check_cart_header_content(context, cart_header_content):
    # assert isinstance(context.driver.find_element(*CART_HEADER).text, object)
    assert CART_HEADER_EXPECTED in context.driver.find_element(*CART_HEADER).text, f'Expected {CART_HEADER_EXPECTED}, but got {cart_header_content}'