*** Settings ***
Library    ../libraries/table_keywords.py
Resource   ../resources/const.robot

*** Test Cases ***
Count Different Items
    [Documentation]  Test to verify the number of different items on the page
    Open Page  ${URL}
    ${table} =  Get Table For Testing  ${ELEMENT}   7
    Get Different Items From    ${table}    5