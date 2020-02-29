# Created by rev19 at 2/15/2020
Feature: Fire Tablets menu
  # Enter feature description here

  Scenario: User can see all menu items under Fire Tablets menu
    Given Open Amazon main page
    When Click Hamburger Menu
    And Click Fire Tablets
    Then Menu will display 16 items

