# Data structures in python 

# Lists and dictionaries are useful structures to 
# house data

dog1 = {'name': 'Buck', 'age': 12, 'color': 'black'}
dog2 = {'name': 'Jeff', 'age': 7, 'color': 'golden'}
dog3 = {'name': 'Greg', 'age': 2, 'color': 'crimson'}

allDogs = []
allDogs.append(dog1)
allDogs.append(dog2)
allDogs.append(dog3)
print(allDogs)

# [{'name': 'Buck', 'age': 12, 'color': 'black'},
# {'name': 'Jeff', 'age': 7, 'color': 'golden'},
# {'name': 'Greg', 'age': 2, 'color': 'crimson'}]

# The above is a simple data structure, it's a list 
# containing dictionaries, this is a way to model data
# and real world things in a way for python to 
# understand 