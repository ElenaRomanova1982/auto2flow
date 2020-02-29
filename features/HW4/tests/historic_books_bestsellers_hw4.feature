# Created by rev19 at 2/21/2020
Feature: Goods count from the search
  # 2. Create a test case that count historic books
  #1.1 Open main amazon page
  #1.2 Send “history book”
  #1.3 Count how much books would be shown in result list
  #1.4* If last book has “Best Seller” label, will add it in the cart (go to page of book)
  #or
  #1.4* If first book has price higher 10$, will add it in the cart (go to page of book)

  Scenario: User can find historic books through the search,
            count result and add to the cart those
            with label "Best Seller"
    Given Open Amazon main page
    When Search for product historic book
    And Click search button
    Then Check there is 22 historic books shown in the search result
    And Check how many books from search result has label "Best Seller"
    When If first search result has price higher than 10
    When Open product page
    Then Add first item to the cart
    #When If last search result has label "Best Seller"
    #Then Add last good to the cart