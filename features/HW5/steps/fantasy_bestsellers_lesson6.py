from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT_LOCATOR = (By.ID, "twotabsearchtextbox")
SEARCH_SUBMIT_LOCATOR = (By.CSS_SELECTOR, ".nav-search-submit")
SEARCH_RESULT_LOCATOR = (By.CSS_SELECTOR, ".s-result-list .a-section.a-spacing-medium")#***  .s-result-list.s-search-result
SEARCH_RESULTS_BESTSELLERS_LOCATOR = (By.CSS_SELECTOR, ".a-badge-label")

@given('Open main Amazon page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')

@when('Search type {search_request}')
def search_text(context, search_request):
    search = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search.clear()
    search.send_keys(search_request)
    search_submit = context.driver.find_element(*SEARCH_SUBMIT_LOCATOR)
    search_submit.click()

@then('Count how much {badge_text} bages on page')
def count_results(context, badge_text):
    search_results = context.driver.find_elements(*SEARCH_RESULT_LOCATOR)
    print(search_results)
    counter = 0
    for search_result in search_results:
        search_result_badge = search_result.find_elements(*SEARCH_RESULTS_BESTSELLERS_LOCATOR) # start to comment at this row
        #print(len(search_result_badge))
        if len(search_result_badge) > 0:
            #print(search_result_badge[0].text)
            if badge_text == search_result_badge[0].text:
                counter += 1
       #try:
            #search_result_badge = search_result.find_element(*SEARCH_RESULTS_BESTSELLERS_LOCATOR)
            #print(search_result_badge)
            #if badge_text == search_result_badge.text:
                #counter += 1
       #except:
           #pass
    print(counter)              # return 0 ???? look again later
#else:                          doesnt work???
    #print(f'result not found')     doesnt work???


