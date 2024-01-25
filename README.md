## Prerequisites
- Python 3
- Robot Framework
- Selenium
- Change pref variable in libraries/table_keywords.py and adjust it with your path same should be done in test_5.robot for ${DIRECTORY} variable

## Installation

- Install Python, Robot Framework and Selenium Library if they are not already installed.
- Open a terminal or command prompt window and navigate to the project directory.
- Install the necessary libraries by running the following command:
'''
pip install -r requirements.txt
'''

## Running the Tests

- Run the tests using the following command:
'''
robot tests/
'''
- To run a specific test, specify the path to the test file:
'''
robot tests/test_file.robot
'''

## Customization

- You can customize the automation by modifying tests and adding your own keywords.

## Debugging the Tests

- After tests or test execution log.html file created

## Project structure
```
├── downloads 
├── liraries
    ├── table_keywords.py
├── resources
    ├── const.robot
├── tests
    ├── test_1.robot
    ├── test_2.robot
    ├── ...    
├── README.md    
├── requirements.txt
```