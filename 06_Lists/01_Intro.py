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

print(myList[-1])
print(myList[-2])


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