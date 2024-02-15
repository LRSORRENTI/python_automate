import re
import pyperclip

# Phone number regex
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s|-)  # first separator
\d\d\d  # first three digits
-       # second separator
\d\d\d\d       # last four digits 
(((ext(\.)?\s)|x) # extension word part
(\d{2,5}))? 
)    # extension number part(optional)
''', re.VERBOSE)

# Email address regex
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

# Get text from clipboard
text = pyperclip.paste()

# Extract phone numbers and email addresses
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# Clean up phone numbers
allPhoneNumbers = [phoneNumber[0] for phoneNumber in extractedPhone]

# Pair phone numbers with email addresses
pairs = list(zip(allPhoneNumbers, extractedEmail))

# Convert to dictionary or keep as a list of lists
# pairs_dict = dict(pairs)  # Uncomment this line if you want a dictionary

# Copy results to clipboard
results = '\n'.join(f'{phone}: {email}' for phone, email in pairs)
pyperclip.copy(results)

print(results)
# 479-205-4874: jmckay67@aol.com
# 678-560-3485: tjordan@msn.com