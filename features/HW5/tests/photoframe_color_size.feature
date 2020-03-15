# Created by rev19 at 3/5/2020
Feature: Photoframe color and size choice
  # Enter feature description here

  Scenario: Check every size option for photoframe on amazon
    Given Open Amazon photoframe page
    When Get all photoframe choice options
    Then Check every choice option has description
    And Chose 7 inch frame and add it to the cart