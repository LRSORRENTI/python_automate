# Recap

- To import selenium, you need to run: from selenium import webdriver

- To open the browser: browser = webdriver.Firefox()

- To send the browser to a url: browser.get('https://inventwithpython.com')

- The browser.find_elements_by_css_selector() method will return a list of WebElement objects

- WebElement objects have a text variable containing the elements HTML in a string

- The click() method will click on an element in a browser

- The send_keys() method will type into a specified field in a browser

- The submit() method can be used to simulate pressing a button

- The browser can also be controlled via: back(), forward(), refresh(), quit()
