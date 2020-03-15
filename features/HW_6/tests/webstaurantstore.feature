# Created by rev19 at 3/12/2020
Feature: Search option, Search result, Cart functionality
  Testcase steps:
Go to https://www.webstaurantstore.com/
Search for 'stainless work table'.
Check the search result ensuring every product item has the word 'Table' its title.
Add the last of found items to Cart.
Empty Cart.

  assertion take from colors py dinamic word {search_product}=table in  description locator.text, collect all element
  click last_result = tables_on_page[-1]  last_result .click(), find add_to_cart.click , find empty_cart.click


  Scenario: User can search for product, find products that include search name, add product to the cart, empty the cart
    Given Open webstaurantstore page
    #Given Open "https://www.webstaurantstore.com" page  ???
    When Search for stainless work table
    And Verify that every search result has word Table in description
    Then Add last of found item to the cart
    And Empty Cart