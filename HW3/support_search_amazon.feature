# Created by rev19 at 2/7/2020
Feature: Support search
  # Enter feature description here

  Scenario: User can search for support
    Given Open Amazon main page
    When Open Help page
    And Search for Cancel order
    Then Cancel Items or Orders is on the search result

