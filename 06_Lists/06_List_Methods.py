# List methods 

# List methods like append and insert can only 
# be called on lists

days = ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun']

# All list items above have a method availble on them 
# called the index() method 
thurs = days.index('Thurs')
print(thurs) 
# 3

sat = days.index('Sat')
print(sat)
# 5

# Note if you have duplicate strings or values the 
# index method returns the first one it finds: 

friends = ['John', 'Dave', 'Chris', 'Dave']
print(friends.index('Dave'))
# 1
print(friends)
# ['John', 'Dave', 'Chris', 'Dave']

friends.append('Samuel')
friends.insert(2, 'Jacob')

print(friends)
# ['John', 'Dave', 'Jacob', 'Chris', 'Dave', 'Samuel']
friends.insert(-1 , 'Michael')
print(friends)
# ['John', 'Dave', 'Jacob', 'Chris', 'Dave', 'Michael', 'Samuel']

# Also note, when calling the append method it does 
# mutate the list for every instance after:

friends.append('Kyle')
friends.append('Beth')
friends.insert(3, 'Matt')

print(friends)

# Lists also have a .remove() method, 

friends.remove('Matt')
print(friends)

# the sort() method: 

numList = [2, 77, 1, 55, 37, 10, 9, 3, 88, 22, 99, 75]
print(numList)
# [2, 77, 1, 55, 37, 10, 9, 3, 88, 22, 99, 75]

numList.sort()
print(numList)
# [1, 2, 3, 9, 10, 22, 37, 55, 75, 77, 88, 99]

# .sort also sorts string lists ASCII-betically,
# not alphabetically, but ASCII, which means 
# uppercase strings come before lowercase 

artists = ['Van Gogh', 'Rembrandt', 'Monet', '12',  'Frida Kahlo', 'Da Vinci']
print(artists)
# ['Van Gogh', 'Rembrandt', 'Monet', 'Frida Kahlo', 'Da Vinci']

artists.sort()
print(artists)
# ['12', 'Da Vinci', 'Frida Kahlo', 'Monet', 'Rembrandt', 'Van Gogh']

# You can also reverse sort by passing in a boolean:

artists.sort(reverse=True)
print(artists)
# ['Van Gogh', 'Rembrandt', 'Monet', 'Frida Kahlo', 'Da Vinci', '12']

# ASCII-BETICALLY:
listings = ['small house', 'Small house', 'big house', 'BIG HOUSE', 'z', 'Z']
print(listings)
# ['small house', 'Small house', 'big house', 'BIG HOUSE', 'z', 'Z']    

listings.sort()
print(listings)
# ['BIG HOUSE', 'Small house', 'Z', 'big house', 'small house', 'z'] 

# But you can pass in a key to sort by true alphabetica

listings.sort(key=str.lower)
print(listings)
# ['BIG HOUSE', 'big house', 'Small house', 'small house', 'Z', 'z'] 