# String Methods 

# As a note, strings are immutable, they cannot 
# be modifed in place 

# upper(), and lower() methods, these will 
# take an input string, and convert it to 
# upper or lower case 

name = 'Luke'
name2 = 'JOHN'
print(name.upper(), name2.lower())
# LUKE john

# These methods are useful when needing to ensure 
# case sensitivity, if you had a small program 
# like: 

# ask = input()
# if(ask == 'yes'):
#     print('play again')
# else: print('Must be lower case yes')

# or you could lowercase the input straightaway 
# using method chaining:

# askTwo = input().lower()

# then the input will aloways be converted to lowercase 
# first

print(name.isupper()) # False 
print(name2.isupper()) # True

# there are many boolean resolving methods like: 

name.isalpha() # checks if letters only 
name.isalnum() # checks if letter and numbers only  
name.isdecimal() # checks if numbers only 
name.isspace() # checks if has whitespace only 
name.istitle() # checks if titlecase only

phrase = 'hello world'
print(phrase[5].isspace()) # True
title = 'The Title Case Is All Words In A String\
         Have Uppercase'
print(title.istitle()) # True

# You can also use the title method to change a 
# string to title case: 

myTitle = 'this is initially a lowercase title'
print(myTitle)
# this is initially a lowercase title
myTitle = myTitle.title()
print(myTitle)
# This Is Initially A Lowercase Title

