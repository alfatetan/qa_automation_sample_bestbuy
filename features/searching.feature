Feature: Searching results testing
    Checking relevant results after searching several items

    Background: Common requirements to execute this test
        Given Navigate to BestBuy
        And Maximize browser's window

    Scenario: Display computer's memory positions
        When Item "computer memory" was input into searching field
        # Then All results should contain "memory" in each position
        