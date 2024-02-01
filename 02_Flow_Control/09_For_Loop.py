# FOR LOOPS 
'''
For loops are used to specify how many times 
a code block should repeat
'''

print('My name is ')
for i in range(5):
    print('Jimmy five times ' + str(i))
'''
My name is 
Jimmy five times 0
Jimmy five times 1
Jimmy five times 2
Jimmy five times 3
Jimmy five times 4
'''

# whie loop equivalent:
idx = 0
while(idx < 5):
    print('Jimmy five times of while loop ' + str(idx))
    idx = idx + 1

'''
Jimmy five times of while loop 0
Jimmy five times of while loop 1
Jimmy five times of while loop 2
Jimmy five times of while loop 3
Jimmy five times of while loop 4
'''


total = 0;
for i in range(101): 
    total = total + i
    print(total)
# 5050

print(range(10))
# range(0, 10)
# range allows two or three arguments, if 
# only one is passed in it defaults to 0

# But if we pass in the first argument as well 
# we can specify the range for the while loop 

totalTwo = 0;
for i in range(50, 101): 
    totalTwo = totalTwo + i
    print(totalTwo)
# 3825
    
# Range can be called with three arguments, 
# range(start, end, incrementByThisNum)
    
totalThree = 0;
for i in range(0, 11, 2): 
    totalThree = totalThree + i
    print(totalThree)
    # 30


for i in range(5, -1, -1): 
    print('count down from ' + str(i))
    '''
    count down from 5
    count down from 4
    count down from 3
    count down from 2
    count down from 1
    count down from 0
    '''