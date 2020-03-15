from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#locators
DRESS_COLORS_BUTTON = (By.CSS_SELECTOR, "ul.a-unordered-list.a-button-list.a-button-toggle-group li") #"#variation_color_name ul[role='radiogroup'] li"
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@given('Open Amazon dress page')
def open_dress_page(context):
    context.driver.get('https://www.amazon.com/dp/B07W36XZ8V')

@when('Get all dress colors')
def get_all_colors(context):
    dress_colors = context.driver.find_elements(*DRESS_COLORS_BUTTON)  #didn't work: context.dress_colors = context.driver.find_elements(*DRESS_COLORS_BUTTON)
    print(len(dress_colors))

@then('Check every color has description')
def color_has_description(context):
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    dress_colors = context.driver.find_elements(*DRESS_COLORS_BUTTON)
    for dress_color in dress_colors:  #didn't work: in context.dress_colors
        dress_color.click()
        print(color_title.text)
        print(dress_color.get_attribute('title'))
        assert color_title.text in dress_color.get_attribute('title'), f"Expected {color_title.text} in{dress_color.get_attribute('title')}"