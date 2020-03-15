# Created by rev19 at 3/11/2020
Feature: #Enter feature name here
  get all elements to array, find again and call by index, assert by url
  *. [Loops] Make a test case which:
Clicks on Best Sellers link on the top menu
Clicks on each top link and verify that new page opens
  
  Scenario: User can click Bestsellers categories button to open appropriate page
    Given Open Amazon main page
    When Open Amazon Bestsellers page
    #When Collect all categories from Bestsellers page
    Then Verify that every cagetory button will open appropriate page

