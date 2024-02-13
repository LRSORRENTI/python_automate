# REGEX BASICS 

# Regex is often used for pattern matching

# Take phone numbers as an example, as a human 
# it's easy to recognize that this:

# 444-555-1000 looks like a phone number, but 
# something like: 
# 444,152,198,5000 is not a phone number, let's 
# write a function below that will return true 
# or false if the REGEX pattern matches  

def isPhoneNumber(text):
    if len(text) > 12:
        print('Text longer than 12 chars')
        return False 
    # below we'll use a for loop to ensure 
    # all chars starting at index 0, and going 
    # up to but not including 3 are 
    for i in range(0, 3):
        if not text[i].isdecimal():
            print(False)
            return False
    if text[3] != '-':
        print('char at index 3 missiing -')
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            print(False)
            return False 
    if text[7] != '-':
        print('char at index 7 missiing -')
        return False
    if i in range(8, 12): 
        if not text[i].isdecimal():
            print(False)
            return False 
    print(True)
    return True


isPhoneNumber('422- 123-4567')
# True
isPhoneNumber('422-1234567')
# char at index 7 missiing -
isPhoneNumber('Hello')
# False

### This is a lot of if checks in the isPhoneNumber 
# function, imagine there are other conditions, 
# We'd need to keep adding if checks 

# REGEX helps make these sorts of pattern matches 
# much more streamline 