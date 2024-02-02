# Pythons built in functions

# Like many other langauges python has some 
# useful functions built into the language itself 
# Some of which we've used already like print(),
# input(), and len(). But python also comes with
# modules known as the:

# STANDARD LIBRARY

# Before you can use the functions in a module, you 
# must first import them

import random 

# For example importing random exposes various 
# methods from the random module like the randint 
# method which takes two int arguments and returns 
# a random number between the two 

random.randint(1, 10)

def printRand(): 
    print(random.randint(1, 10))

printRand()