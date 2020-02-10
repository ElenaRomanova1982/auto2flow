from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# locators:
PRODUCTS_FOUND = (By.CSS_SELECTOR, "div.sg-row div img.s-image")
ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
CART_COUNT= (By.ID, "nav-cart-count")
ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, "h1")
GO_TO_CART_BUTTON = (By.ID, "hlb-view-cart-announce")
PRODUCT_IN_THE_CART_NAME = (By.CSS_SELECTOR, "span.a-size-medium.sc-product-title")


# other constants:
CART_COUNT_EXPECTED = "1"
ADDED_TO_CART_MESSAGE_EXPECTED = "Added to Cart"
PRODUCT_NAME_EXPECTED = "Fisher-Price"

@when ('Click on product from search result')
def click_product_search_result(context):
    context.driver.find_element(*PRODUCTS_FOUND).click()
    sleep(4)

@when ('Add product to the cart')
def add_product_to_the_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(4)

@then ('Cart has {count} item')
def check_cart_count(context, count):
    assert CART_COUNT_EXPECTED in context.driver.find_element(*CART_COUNT).text, f'Expected {CART_COUNT_EXPECTED}, but got {count}'

@then ('{message} displayed on the page')
def check_added_to_cart_message(context, message):
    assert ADDED_TO_CART_MESSAGE_EXPECTED in context.driver.find_element(*ADDED_TO_CART_MESSAGE).text, f'Expected {ADDED_TO_CART_MESSAGE_EXPECTED}, but got {message}'

@then ('Open the Cart page')
def open_the_cart_page(context):
    context.driver.find_element(*GO_TO_CART_BUTTON).click()

@then('Product {product_name} is in the Cart')
def check_product_name_in_the_cart(context, product_name):
    assert PRODUCT_NAME_EXPECTED in context.driver.find_element(*PRODUCT_IN_THE_CART_NAME).text, f'Expected {PRODUCT_NAME_EXPECTED}, but got {product_name}'

