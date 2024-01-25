*** Settings ***
Library    ../libraries/table_keywords.py
Resource   ../resources/const.robot

*** Variables ***
${DIRECTORY} =  /home/oleh/Documents/kineti_proj/downloads/
${ZIP_FILE_LINK} =  Office Supply Sales sample data workbook
${ZIP_FILE_NAME} =  SampleData.zip
${EXEL_FILE_NAME} =  SampleData.xlsx

*** Test Cases ***
Excel Download Test
    [Documentation]  Test to verify the download of an Excel file from the page
    [Setup]     Check And Clean Directory    ${DIRECTORY}
    [Teardown]  Check And Clean Directory    ${DIRECTORY}
    Open Page  ${URL}
    Download File  ${ZIP_FILE_LINK}
    Extract Zip File    ${DIRECTORY}  ${ZIP_FILE_NAME}
    Verify File Download  ${DIRECTORY}  ${EXEL_FILE_NAME}