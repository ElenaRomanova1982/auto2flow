#from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC  #***for explicit wait

COLORS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name li")
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_cart_button")

@given('Open Amazon bike page')
def open_bike_page(context):
    context.driver.get('https://www.amazon.com/dp/B00465Z1LS')

@when('Get all bikes colors')
def get_all_bike_colors(context):
    context.bike_colors = context.driver.fomd_elements(*COLORS_BUTTON_LOCATOR)

@then('Check that every color has description')
def color_has_description(contex):
    color_title = contex.driver.find_element(*COLOR_TITLE_LOCATOR)
    for bike_color in context.bike_colors:
        bike_color.click()
        print(color_title.text)
        print(bike_color.get_attribute('title'))
        assert color_title.text in bike_color.get_attribute('title')

@then('User can add {need_color} bike to cart')
def add_need_color_bike_to_cart(contex, need_color):
    for bike_color in context.bike_colors:
        if need_color in bike_color.get_attribute('title'):
            bike_color.click()
            sleep(3)
            add_to_cart_button = contex.wait.until_not(EC.element_to_be_clickable(ADD_TO_CART_BUTTON))  #***for explicit wait "element_to_be_clickable" wait_until
                                                                            #***locator without "*" (LOCATOR)
                                                                       # contex.driver.find_element(*ADD_TO_CART_BUTTON)- doesnt need when use EC
                                                # selenium.dev - slenium.webdriver.support.expected_conditions
            add_to_cart_button.click()