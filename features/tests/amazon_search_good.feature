# Created by rev19 at 2/5/2020
Feature: Amazon product search feature
  # Enter feature description here

  Scenario: User can search for the product
    Given Open Amazon main page
    When Search for product Lego
    And Click search button
    Then Assert "Lego" header on page
