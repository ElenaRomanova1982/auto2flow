from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


HELP_BUTTON = (By.XPATH, "//a[contains(text(), 'Help')]")
HELP_SEARCH = (By.XPATH, "//input[@id='helpsearch']")
#QUESTION = "Cancel order"
SOLUTION = "Cancel Items or Orders"
HELP_SEARCH_GO = (By.XPATH, "//input[@class='a-button-input']")
HELP_CONTENT = (By.XPATH, "//div[@class='help-content']")


@when ('Open Help page')
def open_amazon_help_page(context):
    context.driver.find_element(*HELP_BUTTON).click()

@when ('Search for {question}')
def search_for_question(context, question):
    find_solution = context.driver.find_element(*HELP_SEARCH)
    find_solution.clear()
    find_solution.send_keys(question)
    sleep(5)
    context.driver.find_element(*HELP_SEARCH_GO).click()

@then('{solution} is on the search result')
def check_solution_is_relevant(context, solution):
    assert SOLUTION in context.driver.find_element(*HELP_CONTENT).text, f'Expected {SOLUTION}, but got {solution}'
#assert 'cancel' in driver.current_url           #find_element(By.XPATH, "//div[@class='g']").text
