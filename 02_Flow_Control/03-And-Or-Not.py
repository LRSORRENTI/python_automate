# In python there are three boolean operators called 
# AND, OR, NOT 

print(True and True)
# true 

print(True and False)
# false 

# When using the and operator, true and true is the 
# only time it will evaluate to true 

# True and True: True
# True and False: False
# False and False: False 
# False and True: False 

# The Or operator will evaluate to true if 
# either value returns true 

print(True or False);
# true

# the not operator will evaluate to the opposite always
print(not True)
# false 

print(not False)
# true 

myAge = 20
myPet = 'Dog'

print(myAge > 10 and myPet == 'Cat')
# false 

print(myAge > 10 and myPet == 'Dog')
# true 