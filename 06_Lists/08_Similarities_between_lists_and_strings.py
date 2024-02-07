# Similarities between lists and strings,
# strings themselves are like lists of characters 

name = 'Luke'
print(list(name))
# ['L', 'u', 'k', 'e']

# Many things available on lists, are also 
# available with strings, indexing, slicing,
# using for loops, len, in and not in

fruit = 'watermelon'
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
# values and save themselves, but it can't be 
# directly reassign letters within a string

wat = fruit[0: 3]
print(wat)
# wat 
# wat.append('ermelon')
# print(wat)
#     wat.append('ermelon')
#     ^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'append'

watList = []
watList.append(wat + 'ermelon')
print(watList)

