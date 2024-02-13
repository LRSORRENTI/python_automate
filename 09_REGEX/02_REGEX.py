# In python there is a REGEX module called re 

import re 

message = 'call me at 415-555-7767 or at 123-555-5555'

# Note, you'll usually always pass in r strings to 
# the .compile method, this is because REGEX makes 
# frequent use of the '\' character 

# \d means we're searching for a digit at the start,
# it's actually \d\d\d since the first three of the 
# phone number pattern are digits 
# then we specify the dash

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# And usually we assign the re.compile to what's 
# known as a match object, often used as 'mo' or 
# 'matcho' or 'matchObject

matchoComacho = phoneNumRegex.search(message)
print(matchoComacho.group())
# the group method returns the first instance it 
# finds for the pattern
# 415-555-7767

# While the finadall method will return every 
# instance of the specified pattern in a list

matchoComacho = phoneNumRegex.findall(message)
print(matchoComacho)
# ['415-555-7767', '123-555-5555']

# So in this file, which is doing the same exact thing 
# as 01_REGEX_BASICS.py, except it's 6 lines of code 
# instead of however many if checks and lines from 
# that file 