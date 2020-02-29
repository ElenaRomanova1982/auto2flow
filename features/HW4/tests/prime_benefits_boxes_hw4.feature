# Created by rev19 at 2/22/2020
Feature: #Enter feature name here
  # Enter feature description here   3. Create a test case that will
  # open amazonprime page: https://www.amazon.com/amazonprime
  # And verify there are 4 boxes:


  Scenario: # There is 5 prime benefits boxes displayed on amazonprime page
    Given Open AmazonPrime page
    #When Find Prime Benefits Boxes on the upper part of the webpage
    Then There is should be 5 Boxes with information about Benefits of Prime membership
