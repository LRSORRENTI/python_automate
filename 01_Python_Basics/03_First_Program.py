# This program says hello and asks for a name

print('Hello world')
print('What is your name?')
# ask for their name 
myName = input()

print("It's great to meet you " + myName)
print('The length of your name is: ')
print(len(myName)) # The len prints the string length
print("What is your age? ")
# ask for age 
myAge = input()

print("You will be " + str(int(myAge) + 1) + ' next year')
# The str(int(myAge) + 1)

# the str and int functions will return string and integer 
# values of what's passed into them so (int(myAge)) will grab 
# the myAge string and turn it into an int to + 1
# then the outer str function takes that and brings it 
# back into string form 

"""$ py 03_First_Program.py 
Hello world
What is your name?
Luke
It's great to meet you Luke
The length of your name is:
4
What is your age?
30
You will be 31 next year"""

# In addition to str and int, there is a float function, 

print(float(20)) # 20.0

# Performing arithmetic operations on a string is 
# not possible, it must always be converted to an 
# integer using int(value) first then perform the 
# operation, and can be converted back using str()
# if needed 

stringNum = '25'
myNum = 35
print(str(int(stringNum) + float(myNum) + 0.1)) # 60.1