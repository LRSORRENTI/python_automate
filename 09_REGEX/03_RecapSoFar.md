# Recap

- Regular expressions are like a mini-language specifically used to pattern match. Writing a few lines of REGEX is often much simpler than huge if check conditional blocks

- REGEX is often using '\' for pattern matching, so always remember to use pythons raw strings like str = r''

- The 're' module is used, import re to expose the built in methods

- Call re.compile saved to a regex object like: regexObject = re.compile

- Call the .search method and save it to a match object like mo = regexObject.search

- Call group() to return the first instance of the specified pattern OR the findall() method to return a list of all found matches
