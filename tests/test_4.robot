*** Settings ***
Library    ../libraries/table_keywords.py
Resource   ../resources/const.robot

*** Test Cases ***
Most Expensive Item Test
    [Documentation]  Test to verify the most expensive item on the page
    Open Page  ${URL}
    ${table} =  Get Table For Testing  ${ELEMENT}   7
    Get Most Expensive Item    ${table}  275.00