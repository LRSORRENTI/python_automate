# Dictionaries are mutable, like lists, if you make 
# a change to a dictionary without a deep copy, it 
# will reference and change the orignal:

dictionary1 = {
    'alpha': 'a',
    'bravo': 'b',
    'charlie': 'c',
    'delta': 'd'
}

print(list(dictionary1.keys()))
# ['alpha', 'bravo', 'charlie', 'delta']
print(list(dictionary1.values()))
# ['a', 'b', 'c', 'd']
print(list(dictionary1.items()))
# [('alpha', 'a'), ('bravo', 'b'), ('charlie', 'c'), ('delta', 'd')] 

for i in dictionary1.keys():
    print(i)
# alpha
# bravo
# charlie
# delta
for j in dictionary1.values():
    print(j)
# a
# b
# c
# d
    
for i, j in dictionary1.items():
    print((i, j))
# ('alpha', 'a')
# ('bravo', 'b')
# ('charlie', 'c')
# ('delta', 'd')
for i in dictionary1.items():
    print(i)
# ('alpha', 'a')
# ('bravo', 'b')
# ('charlie', 'c')
# ('delta', 'd')
    
# i, j allows for direct access to both the key and 
# value separately, as they are unpacked into two 
# distinct variables.

# i assigns the whole key-value pair tuple to 
# a single variable, requiring you to manually 
# access the key and value through tuple indexing 
# if needed.

# Both loops will print out the same results 
# in your examples because of how the print() 
# function is called, but the mechanism of 
# accessing the key and value within the loop 
# differs.
    
print('alpha' in dictionary1)
# True 