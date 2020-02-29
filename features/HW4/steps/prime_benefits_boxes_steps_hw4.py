from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



PRIME_BENEFITS_BOXES = (By.CSS_SELECTOR, ".card-clickable")


@given('Open AmazonPrime page')
def open_amazon_main_page(context):
    context.driver.get('https://www.amazon.com/amazonprime ')

@then('There is should be {expected_count} Boxes with information about Benefits of Prime membership')
def find_prime_benefits_boxes(context, expected_count):
    prime_benefits_boxes = context.driver.find_elements(*PRIME_BENEFITS_BOXES)
    print(len(prime_benefits_boxes))
    if len(prime_benefits_boxes) > 0:
        assert len(prime_benefits_boxes) == int(expected_count), f'Expected {expected_count}, but got {len(prime_benefits_boxes)}'
        if len(prime_benefits_boxes) == int(expected_count):
            print('Your test passed')
    else:
        print('There is no prime benefits boxes')
        print('found {len(prime_benefits_boxes)}') #probably will not work


