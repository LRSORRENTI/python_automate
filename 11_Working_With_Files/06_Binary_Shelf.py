# The Shelve Module 

# Writing and reading lists, dictionaries and 
# other data structures requires more than just 
# append and write, we use the shelve module to save 
# 'Binary Shelf' files 

import shelve

shelfFile = shelve.open('mydata')
# you can make changes to the shelf file as if it 
# were a dictionary

# you use brackets to specify the key, then assign 
# a value to the key

shelfFile['dogs'] = ['mags', 'rey', 'bear', 'chloe']
print(shelfFile['dogs'])
# ['mags', 'rey', 'bear', 'chloe']
print(list(shelfFile.keys()), list(shelfFile.values()))
# ['dogs'] [['mags', 'rey', 'bear', 'chloe']]
shelfFile.close()
