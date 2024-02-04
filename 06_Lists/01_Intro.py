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