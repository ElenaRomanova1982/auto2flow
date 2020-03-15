from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




#locator
PHOTOFRAME_OPTIONS_LOCATOR = (By.CSS_SELECTOR, "#variation_size_name ul li")
OPTION_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_size_name .selection")
ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

@given('Open Amazon photoframe page')
def open_photoframe_page(context):
    context.driver.get('https://www.amazon.com/dp/B07T7V7XXB')

@when('Get all photoframe choice options')
def get_all_choices(context):
    photoframe_options = context.driver.find_elements(*PHOTOFRAME_OPTIONS_LOCATOR)  #didn't work: context.dress_colors = context.driver.find_elements(*DRESS_COLORS_BUTTON)
    print(len(photoframe_options))

@then('Check every choice option has description')
def option_has_description(context):
    choice_title = context.driver.find_element(*OPTION_TITLE_LOCATOR)
    photoframe_options = context.driver.find_elements(*PHOTOFRAME_OPTIONS_LOCATOR)
    for photoframe_option in photoframe_options:  #didn't work: in context.dress_colors
        photoframe_option.click()
        sleep(3)
        print(choice_title.text)
        print(photoframe_option.get_attribute('title'))
        assert choice_title.text in photoframe_option.get_attribute('title'), f"Expected {choice_title.text} in {photoframe_option.get_attribute('title')}"

@then('Chose {desired_option} frame and add it to the cart')
def add_your_choice_to_the_cart(context, desired_option):
    photoframe_options = context.driver.find_elements(*PHOTOFRAME_OPTIONS_LOCATOR)
    for photoframe_option in photoframe_options:
        photoframe_option.click()
        print(photoframe_option.text)
        if photoframe_option.text == desired_option:  #get_attribute('title') ??? cant find...
            sleep(3)
            add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
            add_to_cart_button.click()
            print(photoframe_option.text)
            break
            #print(photoframe_option.get_attribute('title'))
        # if desired_option in photoframe_option.get_attribute('title'):
        #     photoframe_option.click()
        #     sleep(3)
        #     add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON) #need to handle alert
        #     add_to_cart_button.click()
        #     print(photoframe_option.get_attribute('title'))
    else:
        print('not found')


