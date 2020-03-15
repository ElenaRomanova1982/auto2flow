from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BLOG_LINK_LOCATOR = (By.CSS_SELECTOR, "#main-content a[href*='blog']") #less(By.XPATH, "//div[@id='main-content']//a[text()='Learn more on our blog']")

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

@when('Click to blog Link')
def click_to_block_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog_link.click()
    #wait for the new window or tab
    context.driver.wait.until(EC.new_window_is_opened)
    #context.driver.wait.until(EC.number_of_windows_to_be(2))
    all_windows = context.driver.window_handles#***context.all_windows = - doesnt work
    new_window = context.driver.current_window_handle
    print(new_window, f'New windows Ids')
    print(all_windows, f'All windows Ids')

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to_window(all_windows[1]) #***context.all_windows = - doesnt work
    sleep(10)

@then('Check this has {expected_url}')
def check_page_has_url(context, expected_url):
    assert expected_url in context.driver.current_url
    #print(context.driver.current_url)

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