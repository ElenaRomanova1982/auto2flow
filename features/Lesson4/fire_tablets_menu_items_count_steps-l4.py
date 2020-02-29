from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

# locators:
HAM_MENU = (By.ID, "nav-hamburger-menu")
FIRE_TABLETS = (By.XPATH, "//div[contains(text(),'Fire Tablets')]")  #$x("//div[@id='hmenu-content']//ul[@class='hmenu  hmenu-visible']//a[@data-menu-id='5']")
                                                                    #$x("//div[contains(text(),'Fire Tablets')]")
FIRE_TABLETS_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, "#hmenu-content .hmenu-visible a.hmenu-item:not(.hmenu-back-button)")


# other constants:

@when('Click Hamburger Menu')
def click_hamburger_menu(context):
    ham_menu = context.driver.find_element(*HAM_MENU)
    ham_menu.click()
    sleep(3)

@when('Click Fire Tablets')
def click_fire_tablets(context):
    fire_tablets = context.driver.find_element(*FIRE_TABLETS)
    fire_tablets.click()
    sleep(4)


@then('Menu will display {expected_items_count} items')
def get_fire_tiblets_menu_items(context, expected_items_count):
    fire_tiblets_menu_items = context.driver.find_elements(*FIRE_TABLETS_MENU_ITEMS_LOCATOR)
    print(fire_tiblets_menu_items)
    print(type(fire_tiblets_menu_items))
    print(*fire_tiblets_menu_items, sep="\n")
    print(len(fire_tiblets_menu_items))
    expected_items_count = int(expected_items_count)
    if len(fire_tiblets_menu_items) > 0:
        assert len(fire_tiblets_menu_items) == int(expected_items_count), f'Expected {expected_items_count}, but got {len(fire_tiblets_menu_items)}'
        if len(fire_tiblets_menu_items) == int(expected_items_count):
            print('Your test passed')
    else:
        print('There is no fire_tiblets_menu_items')
        print('found {fire_tiblets_menu_items}')


