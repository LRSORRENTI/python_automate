# Similarities between lists and strings,
# strings themselves are like lists of characters 

name = 'Luke'
print(list(name))
# ['L', 'u', 'k', 'e']

# Many things available on lists, are also 
# available with strings, indexing, slicing,
# using for loops, len, in and not in

fruit = 'watermelon'
print(fruit)
print('water' in fruit)
# True 
print('banana' in fruit)
# False 

for letter in fruit:
    print(letter)
# w
# a
# t
# e
# r
# m
# e
# l
# o
# n
    
# The main takeaway is that lists are mutable, they 
# can change, insert values, remove values, change 
# state 
    
# Strings can not be mutated, you can slice out 
# values and save those, but it can't be 
# directly reassigned letters within that string

wat = fruit[0: 3]
print(wat)
# wat 
# wat.append('ermelon')
# print(wat)
#     wat.append('ermelon')
#     ^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'append'

watList = []
watList.append(wat + 'ermelon!')
print(watList[0])
# watermelon!

# When you assign a list to a variable it creates 
# a REFERENCE

nums =  [1, 2, 3, 6, 7]
listOfNums = nums
listOfNums[1] = 'Hello'
print(listOfNums)
print(nums)
# Above you'll notice we only changed the listOfNums
# index 1 to be hello yet both listOfNums and the 
# original list nums both are: 

# [1, 'Hello', 3, 6, 7]
# [1, 'Hello', 3, 6, 7]

# This is because of REFERENCE in python, which is 
# why even though we only made the change to one 
# of the lists, it's reflected in both lists 