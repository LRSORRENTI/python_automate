# copy.deepcopy() function 

# Sometimes you may need to create a completely 
# separate list without creating a reference, 
# and there's a module, the copy module that 
# facilitates this 

import copy 

# and the copy module exposes a useful method called 
# deepcopy which can create a total copy of the list 
# that can be mutated, and those mutations will not 
# mutate the original list 

dogs = ['Rey', 'Mags', 'Bear']

totalDogs = copy.deepcopy(dogs) 

totalDogs.append('Chloe')

print('Original dogs list: ', dogs)
print('Deep copied dogs list: ', totalDogs)

totalDogs[1] = 'Buck'
print(dogs)
# ['Rey', 'Mags', 'Bear']
print(totalDogs)
# ['Rey', 'Buck', 'Bear', 'Chloe']

# So now we can make any changes to that deep 
# copy as we need without worrying about original 
# list mutation