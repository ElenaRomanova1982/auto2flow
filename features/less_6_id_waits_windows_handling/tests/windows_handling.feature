# Created by rev19 at 3/9/2020
Feature: Window handling feature - user can manipulate with windows and tabs
  # Enter feature description here

  Scenario: User can open and close Today's deals under $25[update scenario name]
    Given Open Amazon page
    When Store original windows
    And Click to blog Link
    And Switch to the newly opened window
    Then Check this has blog.aboutamazon.com
    And User can close new window and switch back to original