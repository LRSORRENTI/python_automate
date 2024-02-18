# Assertions and the assert statement

# Assetions are also used frequently as checks
# to ensure or assert that a condition is met, 
# they are used to help quickly identify the cause 
# of why a program is crashing

# assert False, 'This is an error'

# Let's look at an example using traffic lights

market_2nd = {'north_south': 'green',
              'east_west': 'red'}
def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yelllow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'neither light is red' + str(intersection)



switchLights(market_2nd)

# Assertions are for program errors, not user errors 
