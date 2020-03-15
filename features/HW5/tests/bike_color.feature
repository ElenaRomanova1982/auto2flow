# Created by rev19 at 3/6/2020
Feature: Test scenario for choosing colors
  # Enter feature description here

  Scenario: User can change a product color
    Given Open Amazon bike page
    When Get all bike colors
    Then Check that every bike color has description
    And User can add Orange bike to the cart