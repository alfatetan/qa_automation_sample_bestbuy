from selenium import webdriver

# def before_all():
#     pass

def before_feature(context, feature):
    context.URL = "https://www.bestbuy.com/"

def before_scenario(context, scenario):
    # Init the Chrome browser
    context.driver = webdriver.Chrome()
    # Add the implicitly wait about 3 seconds on default
    context.driver.implicitly_wait(3)

# def before_step(context, step):
#     pass

# def after_step(context, step):
#     pass

# def after_scenario(context, scenario):
#     pass

# def after_feature(context, feature):
#     pass

# def after_all():
#     pass