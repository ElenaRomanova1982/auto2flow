# Created by rev19 at 3/3/2020
Feature: Bestseller in fantasy books
  # Enter feature description here

  Scenario: User can see bestsellers searching for fantasy books
    Given Open Amazon main page
    When Search for product fantasy book
    And Click search button
    Then Check there is 22 fantasy books shown in the search result
    And Count how many books from search result has label "Best Seller"
    #And Check bestseller lable in every result that displayed

    #When If last search result has label "Best Seller"
    #Then Add last good to the cart