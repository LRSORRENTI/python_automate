# Scope

# Scope is an important concept

name = 'Luke'
# name is global scope in this python file 
print(name)
# Luke 

# however if we define a function with 
# the name variable somewhere in the funcion 
# body, it is locally scoped:

hobby = 'running'

def printName():
    name = 'JSON'
    hobbyTwo = 'swimming'
    # however the inner scope of a function 
    # body, like inside here can access 
    # the outer scope, like below we can grab the 
    # globally scope hobby variable 
    print(name, 'enjoys', hobby, 'and', hobbyTwo)
printName()
# JSON 

# below will not work hoever, hobbyTwo is 
# local to the printName function body
# print(hobbyTwo)

def spam():
    eggs = 12
    bacon()
    print(eggs, 'eggs inside spam')

def bacon():
    ham = '1lb'
    eggs = 6
    print(ham, eggs, 'eggs inside bacon')

spam()

# 1lb 6 eggs inside bacon
# 12 eggs inside spam

# as you see above, the spam function calls bacon
# but the eggs variable are local to each specific 
# function body

bird = 'Cardinal'

def printBird():
    print(bird)

def printSecBird(): 
    # print(bird)
    global bird
    bird = 'Blue Jay'
    print(bird)

printBird()
printSecBird()
# Cardinal
# Blue Jay