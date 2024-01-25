*** Settings ***
Library    ../libraries/table_keywords.py
Resource   ../resources/const.robot

*** Test Cases ***
Pencil Less Than 5 Units Test
    [Documentation]  Test to verify if there is a pencil with less than 5 units
    Open Page  ${URL}
    ${table} =  Get Table For Testing  ${ELEMENT}   7
    Check Units By Quantity    ${table}    Pencil    5

# The test fails because the task says "in the form of a test",
# which implies the use of a comparison of something with something.
# Since the question is "are there any items ...", I made this decision.
# For the test to pass you can uncomment line 39 and comment line 38 in /libraries/table_keywords.py
# or specify the requirements for the test.