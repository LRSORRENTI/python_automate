# Try and Exception Statements in Python are instrumental 
# ways of keeping programs flowing safe, you can 
# set them as guards in case of unexpected inputs, 
# if someone for example trys to divide a number 
# by zero below, and we didn't wrap the function in 
# a try except block, the program will crash 

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error, cannot divide by zero')
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# Utilizing try / except blocks are crucial tools,
# as it provides a way to ensure the program doesn't 
# crash if something goes awry, i.e. above where we try 
# to divide a number by zero, without the try except 
# Statement, the program never reaches the 
# print(div42by(1)), it will always crash without 
# the use of the try except guard 

