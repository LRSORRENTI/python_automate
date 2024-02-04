# Intro to Lists in Python 

'''
Lists in python are similar to arrays 
in other languages, 
'''

shoppingList = ['Eggs', 'Sardines', 'Sauerkraut',
                'Vegetables', 'Lentils', 'Milk' ]

'''
Lists are not limited to strings, they can contain
different data types inside the same list 

'''

myList = [1, 'one', True]

# lists can also be accessed at negative indexes, 
# this accesses the item at the last index movin 
# backwards: 

print(myList[-1]) # True
print(myList[-2]) # one


'''
Lists can also lists themselves, often known as a matrix 

'''



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][0])  # Output: 1
print(matrix[1][1])  # Output: 5
print(matrix[2][2])  # Output: 9

# Iterating through the matrix
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()  # for a new line

# 1 2 3
# 4 5 6
# 7 8 9

for row in matrix:
    for item in row:
        print(item)
    print()
# 1
# 2
# 3

# 4
# 5
# 6

# 7
# 8
# 9
    
dog = ['Rey', 10]

# Can perform string concatentation or other 
# data type methods on each list index:

# print(dog[0] + ' is' +  [dog][1] + ' years old')
# Above does not work without str conversion:
print(dog[0] + ' is ' + str(dog[1]) + ' years old')
# Rey is 10 years old


# Slice: 
# You can specify slice in python to return 
# values between two indexes using the indexes 
# separated by a ':' colon

print(shoppingList[1:3])
# ['Sardines', 'Sauerkraut]
print(shoppingList[3:6])
# ['Vegetables', 'Lentils', 'Milk']

# Changing values of list indexes:

# Change any value by passing in the index:

planets = ['Jupiter', 'Mars', 'Pluto', 'Neptune',
           'Venus', 'Mercury', 'Uranus', 'Earth']
planets[2] = 'Pluto is not a planet'

print(planets)
# ['Jupiter', 'Mars', 'Pluto is not a planet',
# 'Neptune', 'Venus', 'Mercury', 'Uranus', 'Earth']

earth = str(planets[7: 8][0])
print(earth) # Earth

# You can omit the first slice index start, and 
# python will default start at index 0
animals = ['Dog', 'Cat', 'Fish', 'Bird']
print(animals[:2]) # ['Dog', 'Cat'] 

# Above is effectively the same as: 
print(animals[0:2]) # ['Dog', 'Cat']

# Omitting the second value in slice will 
# return everything in the list after the 
# specified index: 

print(animals[2:])
# ['Fish', 'Bird']

# Del keyword:
# You can use the del keyword to delete an item 
# in a list:

names = ['Peter', 'John', 'Matthew', 'Judas']
del names[-1]
print(names)
# ['Peter', 'John', 'Matthew']

# len and lists: 
print(len(names)) # 3 
# the len method can also be used to quickly 
# return the length of a list 

# You can also quickly join lists by using '+'
listOne = [1, 2, 3]
listTwo = [4, 5, 6, 'seven']
listThree = ['eight', 'nine', 'ten', True]
joinedLists = listOne + listTwo + listThree
print(joinedLists)
# [1, 2, 3, 4, 5, 6, 'seven', 'eight', 'nine', 'ten', True]

# the '*' can be used to repeat a list a given 
# number of times: 

boolies = [True, False, True, False]
print(boolies * 2)
# [True, False, True, False, True, False, True, False]

# There is also the list function() which will take 
# a value and turn it into a list 

fish = 'Muskellunge'
num = 2

print(list(fish))
print(list(str(num)))

# ['M', 'u', 's', 'k', 'e', 'l', 'l', 'u', 'n', 'g', 'e']
# ['2']

# You can also use the 'in' and 'not in' operators 
# to quickly see if a value exists in a list 

birds = ['cardinal', 'robin', 'blue jay']
print('cardinal' in birds) # True 
print('Crow' not in birds) # True
print('Raven' in birds) # False
