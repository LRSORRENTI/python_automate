def plusOne(number): 
    print(number + 1)
    return number + 1;

plusOne(100)

addedNum = plusOne(100)
print(addedNum)
print(type(None))

# As a note if a function does not include 
# an explicit return, the return value defaults 
# to the None data type

'''
Also notice below:
'''
print("hello")
print('world')

'''
returns 
hello 
world 

in the console, but if you add:
'''

print('hello', end='')
print(' world')