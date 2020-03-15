from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


#locators:
SEARCH_FIELD = (By.CSS_SELECTOR, "input#searchval")
SEARCH_GO_BUTTON = (By.CSS_SELECTOR, "button[value='Search']")
PAGE_HEADER = (By.CSS_SELECTOR, "h1")
ITEM_LOCATOR = (By.CSS_SELECTOR, ".gtm-product")
ITEM_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, ".details a.description")
ADD_TO_CART = (By.CSS_SELECTOR, "input[name=addToCartButton]")
VIEW_CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, "a[href*='viewcart']")
EMPTY_CART_LOCATOR = (By.CSS_SELECTOR, ".emptyCartButton")
EMPTY_CART_POPUP = (By.XPATH, "//button[contains(text(),'Empty Cart')]")
CART_ITEM_COUNT = (By.ID, "cartItemCountSpan")





@given('Open webstaurantstore page')
def open_main_page(context):
    context.driver.get('https://www.webstaurantstore.com') #*?? how to do through "page_adress"

#@given('Open {page_address} page')
#def open_main_page(context, page_address):
#    context.driver.get({page_address})

@when('Search for {item_name}')
def search_for_item(context, item_name):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.clear()
    search_field.send_keys(item_name)

    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_GO_BUTTON)).click()
    context.driver.wait.until(EC.url_contains('stainless-work-table')) #***check

@when('Verify that every search result has word {key_word} in description')
def verify_search_result_is_correct(context, key_word):
    page_header = context.driver.find_element(*PAGE_HEADER).text
    assert key_word in page_header, f'Expected {key_word}, but got {page_header}'
    print(key_word, f'=> key word')
    print(page_header, f'=> page header')

    item_descriptions = context.driver.find_elements(*ITEM_DESCRIPTION_LOCATOR)

    for item_description in item_descriptions:  #didn't work: in context.dress_colors
       assert key_word in item_description.text, f"Expected {key_word} in{item_description.text}"
       #bodysuit_color.click()
       #print(color_title.text)
       print(item_description.text)

@then('Add last of found item to the cart')
def add_item_to_the_cart(context):
    items = context.driver.find_elements(*ITEM_LOCATOR)
    print(len(items))
    last_item_in_the_search = items[1]
    last_item_in_the_search.find_element(*ADD_TO_CART).click()
    sleep(5)

@then('Empty Cart')
def empty_cart(context):
    view_cart = context.driver.find_element(*VIEW_CART_BUTTON_LOCATOR)
    view_cart.click()
    context.driver.wait.until(EC.element_to_be_clickable(EMPTY_CART_LOCATOR)).click()
    context.driver.wait.until(EC.element_to_be_clickable(EMPTY_CART_POPUP)).click()
    sleep(10)
    expected_count = 0
    cart_item_count = context.driver.find_element(*CART_ITEM_COUNT).text
    print(cart_item_count, f'cart item count')
    assert expected_count == int(cart_item_count), f'Expected {expected_count} items in the cart, but got{cart_item_count}'







"""
#1
@then('Check every bodysuit color has description')
def color_has_description(context):
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    bodysuit_colors = context.driver.find_elements(*BODYSUIT_COLOR_LOCATOR)
    for bodysuit_color in bodysuit_colors:  #didn't work: in context.dress_colors
        bodysuit_color.click()
        print(color_title.text)
        print(bodysuit_color.get_attribute('title'))

       assert color_title.text in bodysuit_color.get_attribute('title'), f"Expected {color_title.text} in{bodysuit_color.get_attribute('title')}"
   #2
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
         
    """