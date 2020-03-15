from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#locators:
SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox') #".nav-search-submit" CSS
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
SEARCH_RESULT_LOCATOR = (By.CSS_SELECTOR, ".s-include-content-margin.s-border-bottom") #" .s-include-content-margin.s-border-bottom"
                                            #".s-result-list.s-search-results > div[data-index]"(lesson)
BEST_SELLER_LABEL = (By.CSS_SELECTOR, ".a-badge-text")#".a-section.a-spacing-medium span.a-badge-label-inner.a-text-ellipsis"
PRICE_LOCATOR = (By.CSS_SELECTOR, ".a-price-whole") #price for kindle ".a-row.a-spacing-mini .a-price-whole"
SEARCH_RESULT_TITLE_LOCATOR = (By.CSS_SELECTOR, "h2 a")
ADD_TO_CART_LOCATOR = (By.ID, "add-to-cart-button")

#other:
#search_result_count = context.driver.find_elements(*BOOKS_ON_THE_PAGE_COUNT_LOCATOR)
#find last element = search_result_count[-1]

@given('Open Amazon main page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Search for product {search_text}')
def search_input(context, search_text):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys(search_text)
    sleep(4)

@when ('Click search button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(4)


@then('Check there is {expected_count} historic books shown in the search result')
def count_search_result(context, expected_count):
    search_result_count = context.driver.find_elements(*SEARCH_RESULT_LOCATOR)
    print(len(search_result_count))
    assert len(search_result_count) == int(expected_count), f'Expected {expected_count}, but got {len(search_result_count)}'

@then('Check how many books from search result has label "Best Seller"')
def count_search_result(context):
    bestsellers_search_result = context.driver.find_elements(*BEST_SELLER_LABEL)
    print(len(bestsellers_search_result))

@when('If first search result has price higher than {price}')
def check_price(context, price):
    first_result = context.driver.find_elements(*SEARCH_RESULT_LOCATOR)[0]
    first_result_price = first_result.find_element(*PRICE_LOCATOR)
    context.compare_price = int(first_result_price.text) > int(price)
    print(context.compare_price)


@when('Open product page')
def open_item_page(context):
    if context.compare_price == True:
        name_of_the_item = context.driver.find_element(*SEARCH_RESULT_TITLE_LOCATOR)
        name_of_the_item.click()

@then('Add first item to the cart')
def add_to_the_cart(context):
    if context.compare_price == True:
        add_to_cart_button = context.driver.find_element(*ADD_TO_CART_LOCATOR)
        add_to_cart_button.click()
        sleep(2)


@when ('Search again')
def repeat_search(context):
    context.execute_steps(f'when Search for product {search_text}') # , f'when Click search button'


@when('If last search result has label "Best Seller"')
def check_label(context):
    last_result = context.driver.find_elements(*SEARCH_RESULT_LOCATOR)[-1]
    last_result_label = last_result.find_elements(*BEST_SELLER_LABEL)
    context.check_label = len(last_result_label) > 0

@then('Add last good to the cart')
def add_to_the_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_LOCATOR)
    add_to_cart_button.click()
    sleep(2)


