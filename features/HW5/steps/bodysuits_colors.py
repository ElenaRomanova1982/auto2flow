from selenium.webdriver.common.by import By
from behave import given, when, then


#variation_color_name

#locator
BODYSUIT_COLOR_LOCATOR = (By.CSS_SELECTOR, "ul.a-unordered-list.a-button-list.a-button-toggle-group li") #"#variation_color_name ul[role='radiogroup'] li"
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection") #variation_color_name

@given('Open Amazon bodysuit page')
def open_bodysuit_page(context):
    context.driver.get('https://www.amazon.com/dp/B0748YL9M4')

@when('Get all bodysuit colors')
def get_all_colors(context):
    bodysuit_colors = context.driver.find_elements(*BODYSUIT_COLOR_LOCATOR)  #didn't work: context.dress_colors = context.driver.find_elements(*DRESS_COLORS_BUTTON)
    print(len(bodysuit_colors))

@then('Check every bodysuit color has description')
def color_has_description(context):
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    bodysuit_colors = context.driver.find_elements(*BODYSUIT_COLOR_LOCATOR)
    for bodysuit_color in bodysuit_colors:  #didn't work: in context.dress_colors
        bodysuit_color.click()
        print(color_title.text)
        print(bodysuit_color.get_attribute('title'))
        assert color_title.text in bodysuit_color.get_attribute('title'), f"Expected {color_title.text} in{bodysuit_color.get_attribute('title')}"