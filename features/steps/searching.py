from selenium import webdriver
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

@step('Item "{item_name}" was input into searching field')
def input_into_search_field(context, item_name):
    search_field = context.driver.find_element(By.XPATH, '//input[@id="gh-search-input"]')
    search_field.send_keys(item_name)
    search_field.send_keys(Keys.ENTER)

# @step('All results should contain "{key_word}" in each position')