  # Created by rev19 at 2/8/2020
Feature: #Enter feature name here
  # Enter feature description here
  #Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty.

  Scenario: Shopping cart is empty for unidentified user
    Given Open Amazon main page
    When Click on Cart icon
    Then Cart is empty displayed in Cart Page header

    # And Cart page is opened (assert by part of url "cart")