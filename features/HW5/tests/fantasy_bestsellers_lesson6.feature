# Created by rev19 at 3/4/2020
Feature: Test scenarios for finding bestsellers
  # Enter feature description here

  Scenario: Count best selers books on page
    Given Open main Amazon page
    When Search type fantasy book
    Then Count how much Best Seller bages on page