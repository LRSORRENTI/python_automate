# Writing functions

'''
When defining a function, use the 'def' keyword 
prefixed before the function name, this keyword 
is always used to prefix function declarations,
similar to in javascript when you define a 
function by prefixing the function keyword:
function hello()
'''

def hello(name):
    print("Hello " + name )
    print("How are you?")
    print("Hello there")

hello("Luke")
# hello('Matt')
# hello('Stephen')

def printLen(str):
    print(str, 'has', len(str), 'characters in length')

printLen('abcdefghijklmnopqrstuvwxyz')

for i in range(5):
    printLen('abcde')