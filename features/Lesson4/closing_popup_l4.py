from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


POPUP_LOCATOR = (By.CSS_SELECTOR, ".otw-white-popup")
POPUP_CLOSE_BUTTONS = (By.CSS_SELECTOR, ".mfp-close")


@given('Open herritage main page')
def open_herritage_main_page(context):
    context.driver.get('https://heritagedoorsandwindows.com/')
    sleep(5)

@when('Popup is displayed')
def popup_displayed(context):
    popup = context.driver.find_elements(*POPUP_LOCATOR)
    sleep(3)
    print(len(popup))
    len_popup = len(popup)
    # doesn't work either? > print('There was {len_popup} popups found on the webpage')
    # doesn't work - why? > print('There was {len(popup)} popups found on the webpage')

@then('Close popup')
def popup_closing(context):
    popup_close_buttons = context.driver.find_elements(*POPUP_CLOSE_BUTTONS)
    sleep(5)
    if len(popup_close_buttons) > 0:
        popup_close_buttons[0].click()
        print('Popup was closed')
    else:
        print('No popups was found')