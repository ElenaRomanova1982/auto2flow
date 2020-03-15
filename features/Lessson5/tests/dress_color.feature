# Created by rev19 at 3/2/2020
Feature: Dress color
  # Enter feature description here

  Scenario: Check every dress color name
    Given Open Amazon dress page
    When Get all dress colors
    Then Check every color has description