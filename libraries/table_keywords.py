import os
import time
import shutil
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
pref = {"download.default_directory": "/home/oleh/Documents/kineti_proj/downloads"}
chrome.add_experimental_option("prefs", pref)
chrome = webdriver.Chrome(chrome_options=chrome)


def get_table_for_testing(element, columns=0, driver=chrome):
    elem = driver.find_element(By.XPATH, element)
    table_text = elem.text
    table_tex_formatted = table_text.split('\n')
    table = [table_tex_formatted[i:i + columns] for i in range(0, len(table_tex_formatted), columns)]
    return table


def get_different_items_from(table, qty):
    items = [i[3] for i in table[1:]]
    assert len(set(items)) == int(qty), f'Items was got: {len(set(items))} but expected: {qty}'


def open_page(page, driver=chrome):
    driver.get(page)


def check_items_less_then_given_quantity(table, qty):
    units = [i for i in table[1:] if int(i[4]) < int(qty)]
    assert units, f'There are no items less than {qty} units'


def check_units_by_quantity(table, item, qty):
    formatted_table_by_item = [row for row in table[1:] if row[3] == item and int(row[4]) < int(qty)]
    assert formatted_table_by_item, f'There are no item {item} less than {qty}'
    #assert not formatted_table_by_item

    # The test fails because the task says "in the form of a test",
    # which implies the use of a comparison of something with something.
    # Since the question is "are there any items ...", I made this decision.
    # For the test to pass you can uncomment line 39 and comment line 38 or specify the requirements for the test


def get_most_expensive_item(table, price):
    assert max(table[1:], key=lambda i: float(i[5]))[
               5] == price, f'Most expensive item price: {max(table[1:], key=lambda i: float(i[5]))[5]}, price: {price}'


def check_and_clean_directory(directory):
    files = os.listdir(directory)

    if files:

        for file in files:
            file_path = os.path.join(directory, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


def download_file(link_text, driver=chrome, timeout=2):
    link = driver.find_element(By.LINK_TEXT, link_text)
    driver.execute_script("arguments[0].click();", link)
    time.sleep(timeout)  # Wait for the file to finish downloading


def verify_file_download(directory, filename):
    path = os.path.join(directory, filename)
    assert os.path.exists(path), f'Path {path} does not exist'


def extract_zip_file(directory, zip_filename):
    zip_path = os.path.join(directory, zip_filename)
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(directory)
