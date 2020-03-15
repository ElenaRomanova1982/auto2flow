# Created by rev19 at 3/10/2020
Feature: Cart will have an item that have been added even after refresh or switching pages
  1. Improve a window handling test case from the class and verify that
  user can add a product from today’s deals into the cart and then go back
  to the previous window, refresh and see cart counter updated to 1:



  Scenario: User can open and close pages, cart items would be saved in memory
    Given Open Amazon page
    When Store original windows
    And Click to blog link
    And Switch to the newly opened window
    And Go back to Amazon
    And Open Todays Deals
    And Choose first category
    And Choose first product from the category
    And Add product to the cart
    And Close this window
    And Close blog window
    And Switch back to original window and refresh the page
    Then Cart has 1 item
