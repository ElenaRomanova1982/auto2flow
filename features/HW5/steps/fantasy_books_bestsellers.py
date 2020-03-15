from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

#locators:
SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.nav-input[value='Go']")
SEARCH_RESULT_LOCATOR = (By.CSS_SELECTOR, ".s-result-list .a-section.a-spacing-medium") #" .s-include-content-margin.s-border-bottom"
                                            #".s-result-list.s-search-results > div[data-index]"(lesson)
BEST_SELLER_LABEL = (By.CSS_SELECTOR, ".a-badge-label")#".a-section.a-spacing-medium span.a-badge-label-inner.a-text-ellipsis"


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

@then('Check there is {expected_count} fantasy books shown in the search result')
def count_search_result(context, expected_count):
    search_result_count = context.driver.find_elements(*SEARCH_RESULT_LOCATOR)
    print(len(search_result_count))
    assert len(search_result_count) == int(expected_count), f'Expected {expected_count}, but got {len(search_result_count)}'

@then('Count how many books from search result has label "Best Seller"')
def count_search_result(context):
    bestsellers_search_result = context.driver.find_elements(*BEST_SELLER_LABEL)
    print(len(bestsellers_search_result))

#@then('Check bestseller lable in every result that displayed')