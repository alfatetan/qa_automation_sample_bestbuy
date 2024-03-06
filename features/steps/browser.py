from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

@step("Navigate to BestBuy")
def start_browser(context):
    '''
    Open the browser and go to the webpage
    IN: Nothing
    OUT: If webpage won't be opened for 4 sec return the error message
    '''
    context.driver.get(context.URL)
    # Explicitly wait unless webpage uploaded
    err_message = f"!!! *** ERROR *** Main page can not be opened !!!"
    footer = Wait(context.driver, 4).until(EC.presence_of_element_located((By.XPATH, "//footer/ul/li[5]")), message=err_message)

@step("Maximize browser's window")
def maximize_browser_window(context):
    '''
    Maximizing browser's window
    '''
    context.driver.maximize_window()