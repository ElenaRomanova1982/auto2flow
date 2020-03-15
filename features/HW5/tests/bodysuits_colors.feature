# Created by rev19 at 3/3/2020
Feature: Dress color
  # Enter feature description here

  Scenario: Check every bodysuit color name
    Given Open Amazon bodysuit page
    When Get all bodysuit colors
    Then Check every bodysuit color has description