# Pythons built in functions

# Like many other langauges python has some 
# useful functions built into the language itself 
# Some of which we've used already like print(),
# input(), and len(). But python also comes with
# modules known as the:

# STANDARD LIBRARY

# Before you can use the functions in a module, you 
# must first import them, and you can import as many 
# as needed by separating them with commas 

import sys, os, math

# Alternatively, you can import things like:

from random import *


# For example importing random exposes various 
# methods from the random module like the randint 
# method which takes two int arguments and returns 
# a random number between the two 

# when using the import syntax: from random import *
# random.randint is not necessary, this type of 
# import directly exposes randint without the 
# need to use dot notation to call it 

# random.randint(1, 10)

def printRand(): 
    print(randint(1, 10))

printRand()

print(randint(50, 60))