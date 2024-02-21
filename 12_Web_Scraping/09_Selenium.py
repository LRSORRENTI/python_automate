# Using Selenium to control a browser 

# Often when accessing a webpage, it requires login
# or JavaScript to work properly, the Selenium 
# module allows you to run a web browser, and control 
# it from a Python program 
from selenium import webdriver

# use the webdriver from selenium and call .Firefox,
# and store it in a broweser object 
# browser = webdriver.Firefox()
options = webdriver.FirefoxOptions.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)
 # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

