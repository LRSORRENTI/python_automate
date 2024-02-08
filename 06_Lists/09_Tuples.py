
mytuple = ("apple", "banana", "cherry")

# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# ExampleGet your own Python Server
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
thistuple = ("grape", "lemon", "peach")
print(thistuple)
# ('grape', 'lemon', 'peach')

# Reassignment of the variable thistuple to a new
# tuple is allowed because you are essentially just 
# pointing the variable to a new memory location that 
# contains the new tuple. 

# This doesn't change the tuple itself but changes 
# what the variable thistuple refers to.

# However, attempting to modify the contents of a 
# tuple directly via something like 
# thistuple[0] = "orange" is not allowed because 
# tuples are immutable. If you try to execute such a 
# statement, Python will raise a TypeError to 
# indicate that you're attempting to perform an 
# operation that violates the tuple's immutability.

# This immutability is what distinguishes tuples 
# from lists, which are mutable and allow for their 
# contents to be changed, added to, or removed after 
# creation.

