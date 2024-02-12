myStr = 'That is Alice\'s cat \n and \
         the \t cat says\" "meow" \" \\ '
print(myStr)

# That is Alice's cat 
#  and the         cat says" "meow" " \

# \ Formats a long string for better readability
# \' Prints a single qoute
# \" Prints a double quote
# \t Adds a tab space 
# \n Adds a line break 
# \\ adds a backslash character

# RAW STRINGS 

# In python you can use raw strings to use many '\' 

newStr = r'that is carlol\'s\ cat '
print(newStr)
# that is carlol\'s\ cat

# MULTI-LINE STRINGS 

# often it's easier to use multi-line strings: 

paragraph = """
    This is a multiline string and can span 
    multiple lines
"""
