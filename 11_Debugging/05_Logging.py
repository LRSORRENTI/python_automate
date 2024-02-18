# Logging 

# Logging is a great way to discern what's happening
# at any given point in a program 

# The logging.basicConfig() function is used to 
# display log messages 

import logging

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - \
                            %(levelname)s - \
                            %(message)s')

# You can also write the logs to a file by adding:

# logging.basicConfig(filename='05_Loggingpy.txt', \
#                     level=logging.DEBUG, \
#                     format='%(asctime)s - \
#                             %(levelname)s - \
#                             %(message)s')

# The above is the proper way to set up logging in 
# python

# Let's test the above with a buggy factorial function

logging.debug('Start of program, before factorial')

def factorial(n):
    logging.info('First line in factorial(%s) ' % (n))
    total = 1
    # for i in range(n + 1):
    # the above is why the program isn't working
    # we're multiplying by 0, we need to set the range 
    # to start at 1 not zero
    for i in range(1, n + 1):
        total *= i
        logging.critical('i currently is %s, total is %s '  %(i, total ))
    print(total)
    logging.info('Return value is %s' %(total))
    return total

factorial(5)

logging.debug('End of program, after factorial')