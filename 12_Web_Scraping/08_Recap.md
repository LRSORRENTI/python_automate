# Recap

- Web pages are plaintext files formatted as HTML

- HTML can be parsed using the BeautifulSoup module

- BeautifulSoup is imported via bs4 module

- Pass the string with the HTML to the bs4.BeautifulSoup() function to get a Soup Object

- The Soup object has a select() method that can be passed a string of a CSS selector for an html tag

- To quickly identify the exact CSS selector, inspect and element in browser tools, then right click and copy selector, or copy css selector

- The select() method will return a list of matching element objects
