import re, pyperclip

# The goal of this is to create a regex to extract 
# every email and phone number from a gigantic 
# file 

# 1. Create a REGEX for the phone numbers 
re.compile(r'''
# 414-555-1234, 555-1234, (414) 555 1234, 
# 555-100 ext 12345, ext. 12345, x12345

# area code (optional)
# first separator
# first three digits
# second separator
# last four digits 
# extension (optional)

''', re.VERBOSE)

# 2. Create a REGEX for the email addresses
# 3. Use pyperclip to get the text off clipboard
# 4. Extract email and password from the text 
# 5. Copy the text to the clip board