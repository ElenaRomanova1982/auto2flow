from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#locators:
BLOG_LINK_LOCATOR = (By.CSS_SELECTOR, "#main-content a[href*='blog']")
BACK_TO_AMAZON_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".GatewayMenu")
TODAYS_DEALS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#nav-xshop a[href*='goldbox']")
TODAYS_DEALS_CATEGORIES_LOCATOR = (By.ID, "dealImage")
PRODUCTS_LOCATOR = (By.CSS_SELECTOR, "#octopus-dlp-asin-stream li")
ADD_TO_CART_BUTTON_LOCATOR = (By.ID, "add-to-cart-button")
CART_COUNT_LOCATOR = (By.ID, "nav-cart-count")




@given('Open Amazon page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')  #ambiguous step
    context.init_window = context.driver.current_window_handle
    #print(init_window, f'Initial window Id')
    all_windows = context.driver.current_window_handle
    print(all_windows, f'All windows Ids')
    #current_window = context.driver.current_window_handle
    #print(current_window)
    #current_window = @given('Open Amazon main page')
    #***if link will open in new tab - atribute[target="_blank"]

@when('Store original windows')
def store_original_window(context):
    context.init_window = context.driver.current_window_handle
    assert len(context.driver.window_handles) == 1, f"Expected {1} window opened, but got {len(context.driver.window_handles)}"
    print(len(context.driver.window_handles), f'windows opened')

@when('Click to blog Link')
def click_to_block_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog_link.click()
    #wait for the new window or tab
    context.driver.wait.until(EC.new_window_is_opened)
    #context.driver.wait.until(EC.number_of_windows_to_be(2))
    all_windows = context.driver.window_handles#***context.all_windows = - doesnt work
    new_window = all_windows[1]
    #new_window = context.driver.current_window_handle[1]
    print(new_window, f'New window Ids')
    print(all_windows, f'All windows Ids')

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to_window(all_windows[1]) #***context.all_windows = - doesnt work
    sleep(10)
    print(context.driver.current_window_handle)

    for window_handle in context.driver.window_handles:
        if window_handle != context.init_window:
            context.driver.switch_to.window(window_handle)
            break
        else:
            print("Sucesefully switched")

@when('Go back to Amazon')
def go_back_to_main_page(context):
    back_to_amazon_button = context.driver.find_element(*BACK_TO_AMAZON_BUTTON_LOCATOR)
    context.second_window = context.driver.current_window_handle
    print(context.second_window)
    back_to_amazon_button.click()
    context.all_windows = context.driver.window_handles
    context.third_window = context.driver.current_window_handle
    print(context.third_window)
    print(context.all_windows)
    print(context.second_window)
    assert len(context.driver.window_handles) == 3, f"Expected {3} window opened, but got {len(context.driver.window_handles)}"
    print(len(context.driver.window_handles), f'windows opened')
    context.driver.switch_to_window(context.all_windows[2])
    sleep(10)
    print(context.driver.current_window_handle)

@when('Open Todays Deals')
def open_todays_deals(context):
    todays_deals = context.driver.find_element(*TODAYS_DEALS_BUTTON_LOCATOR)
    todays_deals.click()
    sleep(10)
@when('Choose first category')
def chose_first_catogory_from_todays_deals(context):
    todays_deals_categories = context.driver.find_elements(*TODAYS_DEALS_CATEGORIES_LOCATOR)
    first_catogory_from_deals = todays_deals_categories[0]
    first_catogory_from_deals.click()
    sleep(10)

@when('Choose first product from the category')
def choose_first_product(context):
    products = context.driver.find_elements(*PRODUCTS_LOCATOR)
    first_product = products[0]
    first_product.click()
    sleep(10)

@when('Add product to the cart')
def add_to_the_cart(context):
    context.driver.wait.until(EC.presence_of_element_located(ADD_TO_CART_BUTTON_LOCATOR))
    context.driver.find_element(*ADD_TO_CART_BUTTON_LOCATOR).click()

@when('Close this window')
def close_third_window(context):
    context.driver.close()
    sleep(5)
    context.driver.switch_to_window(context.second_window)
    print(context.driver.current_window_handle, f'after switch')


@when('Close blog window')
def close_second_window(context):
    context.driver.close()
    sleep(5)

@when('Switch back to original window and refresh the page')
def switch_to_init_window_and_refresh(context):
    context.driver.switch_to_window(context.init_window)
    print(context.driver.current_window_handle, f'after switch')
    sleep(3)
    context.driver.refresh()
    print(context.driver.current_window_handle, f'after refresh')
@then('Cart has {expected_number} item')
def check_cart_containment(context, expected_number):
    cart_count = context.driver.find_element(*CART_COUNT_LOCATOR).text
    assert expected_number in cart_count, f'Expected{expected_number}, but got {cart_count}'







###*Add libraries: from selenium.webdriver.common.keys import Keys
###* from selenium.webdrier.common.action_chains_import ActionChains
"""
assert len(fire_tiblets_menu_items) == int(
        expected_items_count), f'Expected {expected_items_count}, but got {len(fire_tiblets_menu_items)}'


    @then('Cart has {count} item')
    def check_cart_count(context, count):
        assert CART_COUNT_EXPECTED in context.driver.find_element(
            *CART_COUNT).text, f'Expected {CART_COUNT_EXPECTED}, but got {count}'

@then('User can close new window and switch back to original')
def go_back_to_original_window(context):
    print(context.driver.current_window_handle)
    #new_window = context.driver.current_window_handle
    #new_window.close()
    context.driver.close()
    sleep(5)
    context.driver.switch_to_window(context.init_window)
    print(context.driver.current_window_handle, f'after switch')
    print(context.init_window, f'Init-original window')
    sleep(5)
    
    """