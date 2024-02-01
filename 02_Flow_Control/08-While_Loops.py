"""
# WHILE LOOPS:

While loops are used to make blocks of code execute 
over and over while a given condition remains TRUE


"""

spam = 0

while spam < 5:
    print('spam:',spam, 'spam is less than 5')
    spam = spam + 1;
# spam: 0 spam is less than 5
# spam: 1 spam is less than 5
# spam: 2 spam is less than 5
# spam: 3 spam is less than 5
# spam: 4 spam is less than 5

next = 0
if next < 5:
    print('less than 5')
    next = next + 1
    print(next)

name = ''
while name != 'your name':
    print('please type your name')
    name = input()
print('thanks')

# While loops can be handy when needing a user to enter 
# a valid input, until the user enters whatever is 
# set as the condition, above it's 'your name', it 
# will continue looping

'''
INFINITE LOOPS 

Infinite loops occur when the exit condition for 
a loop is never met: 

infinity = 1
while infinity > 0:
    print('looping forever')
'''

'''
BREAK STATEMENTS 

Break statements are used within loops to check 
for a condition, then break out of the loop 
if that condition is met 

'''

name = ''
while True:
    print('please type in: one')
    name = input()
    if name == 'one':
        break
print('thanks for entering one')

'''
CONTINUE STATEMENTS: 

Like break statements continue statements are also 
used inside loops, when the loop reaches the continue
statement, it jumps back to evaluate the loops current 
condition

'''

faveNum = 0
while faveNum < 5:
    faveNum = faveNum + 1
    if faveNum == 3:
        continue
    print('faveNum is ' + str(faveNum))
'''
Below is the output, and see that when the iteration
reaches three, it jumps back up and skips 3

faveNum is 1
faveNum is 2
faveNum is 4
faveNum is 5
'''

'''
RECAP: 

When an execution reaches the end of a while loop
statement block, it jumps back up to re-check 
the condition

CTRL + C, can be used to break out of an infinite loop 
in the terminal 

A Break statement causes the execution to immediately 
leave the loop without checking the condition

A Continue statement causes the execution to immediately
jump back to the start of the loop and re-check the condition


'''