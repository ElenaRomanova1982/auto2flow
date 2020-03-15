# Created by rev19 at 3/8/2020
Feature: Test scenarios for tooltip


  Scenario: Check when tooltip will hide
    Given Open Amazon main page
    When Sign in tooltip is clickable
    And Sign in tooltip will hide
    Then Tooltip is not clickable

