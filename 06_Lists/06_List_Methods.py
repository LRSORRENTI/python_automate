# List methods 

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