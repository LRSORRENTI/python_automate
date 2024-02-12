# More strings methods 

# startwith and endswith will check for a string 
# that starts with a given set of chars, and 
# ends with a set of chars:

bird = 'cardinal'
print(bird.startswith('bird'))
# False 
print(bird.startswith('card'))
# True 
print(bird.endswith('inal'))
# True

# the join() method will be passed a list of 
# strings and will join them:

punct = ','
print(punct.join(['cats', 'rats', 'bats']))
# cats,rats,bats
space = ' '
print(space.join(['cats', 'rats', 'bats']))
# cats rats bats
newline = '\n\n'
print(newline.join(['cats', 'rats', 'bats']))
# cats

# rats

# bats


# the split() method 
# split is called on a string and returns a list 
# containing all the words inside:

phrase = 'Hello there, general kenobi'
print(phrase.split())
# ['Hello', 'there,', 'general', 'kenobi']