myDogs = {
    'rey': 'German Shepherd',
    'maggie': 'Cava-Corgi'
}

print(myDogs['rey'], myDogs['maggie']) 
# German Shepherd Cava-Corgi

print(myDogs)
# {'rey': 'German Shepherd', 'maggie': 'Cava-Corgi'}

luggage = {
    1234: 'Luggage Combination',
    42: 'The answer'
}

otherLuggage = {
    42: 'The answer',
    1234: 'Luggage Combination'
}

# Also dictionary key value pairs can be in any 
# order, and if they contain the same values, it 
# does return true: 

print(luggage == otherLuggage)
# True 

# Trying to access a key in a dictionary that 
# doesn't exist will return a key error:
# print(luggage[11])
#  line 28, in <module>
#     print(luggage[11])
#           ~~~~~~~^^^^
# KeyError: 11

# IN and NOT IN 

# You can also use in and not in to check if a key 
# exists within a dictionary: 

print(42 in luggage, 43 in luggage, 44 not in luggage)
# True False True
