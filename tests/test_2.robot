*** Settings ***
Library    ../libraries/table_keywords.py
Resource   ../resources/const.robot

*** Test Cases ***
Less Than 5 Units Test
    [Documentation]  Test to verify if there is an item with less than 5 units
    Open Page  ${URL}
    ${table} =  Get Table For Testing  ${ELEMENT}   7
    Check Items Less Then Given Quantity    ${table}    5