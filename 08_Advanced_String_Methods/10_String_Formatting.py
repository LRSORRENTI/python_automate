name = 'Alice'
time = '4pm'
place = 'Main St.'
food = 'pasta'
print('Hello ' + name + " you're invited to a party at " \
      + place + ' at ' + time + ' to eat ' + food )
# Hello Alice you're invited to a party atMain St. at 4pm to eat pasta

# The above is cumbersome to write, so python has 
# string formatting, using '%s' or conversion 
# specifiers 

print("Hello %s, you're invited to a party at %s \
      at %s, we'll be eating %s" %(name, place, \
                                   time, food))
# Hello Alice, you're invited to a party at Main St.       at 4pm, we'll be eating pasta