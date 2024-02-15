import re, pyperclip

# The goal of this is to create a regex to extract 
# every email and phone number from a gigantic 
# file 

# 1. Create a REGEX for the phone numbers 
phoneRegex = re.compile(r'''
# 414-555-1234, 555-1234, (414) 555 1234, 
# 555-100 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)  # first separator
\d\d\d  # first three digits
-       # second separator
\d\d\d\d       # last four digits 
(((ext(\.)?\s)|x) # etx word part
(\d{2,5}))? 
)    # extension number part(optional)

''', re.VERBOSE)

# 2. Create a REGEX for the email addresses
emailRegex = re.compile(r'''
# Emails can be more demanding, since before the @ 
# emails can have '.,+_, and many other special chars

 # name 
# below is the range of characters we'll search for in 
# the email
[a-zA-Z0-9_.+]+
@               # @ symbol 
[a-zA-Z0-9_.+]+ # domain name part                                          
                        

''', re.VERBOSE)

# 3. Use pyperclip to get the text off clipboard
text = pyperclip.paste()

# 4. Extract email and password from the text 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)
# ['435-270-1776', '957-844-5572', '345-325-5854']
# print(extractedEmail)

# 5. Copy the text to the clip board
results = '\n'.join(allPhoneNumbers) + '\n' \
+ '\n'.join(extractedEmail)

print(results)