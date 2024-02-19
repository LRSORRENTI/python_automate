# Parsing HTML using the beautiful soup module

# For many websites, in order to get the text data 
# we need, we'll need to actually parse the HTML

# Beautiful soup helps us accomplish this 

import bs4
import requests

# Let's test this by scraping pricing data from 
# an amazon page 

res = requests.get('https://en.wikipedia.org/wiki/Order_of_operations')

res.raise_for_status()
print(res.raise_for_status())

# We download the data with requests.get like before
# then pass res.text to the BeautifulSoup method

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# now the soup variable is ready to find specified 
# html elements 

elems = soup.select('#Mixed_division_and_multiplication')
print(elems[0].text.strip())
