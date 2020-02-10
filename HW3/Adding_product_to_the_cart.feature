# Created by rev19 at 2/8/2020
Feature: #Enter feature name here
  # Enter feature description here
  #Create your own test case to add any product
  # you want into the cart, and make sure
  # it’s there (check for the number of items
  # in the cart OR open the cart and verify
  # it’s there, up to you!)

  Scenario: Adding product to the cart
    Given Open Amazon main page
    When Search for product Fisher-Price
    And Click search button
    And Click on product from search result
    # And Open product page
    And Add product to the cart
    Then Cart has 1 item
    And Added to Cart displayed on the page
    And Open the Cart page
    And Product Fisher-Price is in the Cart