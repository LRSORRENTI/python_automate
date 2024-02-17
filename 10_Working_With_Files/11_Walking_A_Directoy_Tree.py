# Walking through directory trees, this concept is 
# very important concept

# If you're tasked with working with or changing 
# huge amounts of files, names, extensions of files 
# etc.. doing that one by one in the file explorer 
# will take a long time depending on how many you 
# need to modify

# Python exposes a method called os.walk()
import os 
import shutil
# os.walk, is passed a root folder path as an 
# argument

# The return value is usually used in for loops 
# for folderName, subfolders, filenames in os.walk('C:\\delicious'):
#     print('The folder is ' + folderName)
#     print('The subfolders in ' + folderName + 'are' + str(subfolders))
#     print('The files in ' + folderName + 'are' + str(filenames))
#     print()
    
# The folder is C:\delicious
# The subfolders in C:\deliciousare['breakfastFavorites', 'tastyFood']
# The files in C:\deliciousare['testingPythonAutomateTheBoringStuff.txt']

# The folder is C:\delicious\breakfastFavorites
# The subfolders in C:\delicious\breakfastFavoritesare['eggs', 'sandwiches']
# The files in C:\delicious\breakfastFavoritesare[]

# The folder is C:\delicious\breakfastFavorites\eggs
# The subfolders in C:\delicious\breakfastFavorites\eggsare[]
# The files in C:\delicious\breakfastFavorites\eggsare['overeasy.txt', 'scrambled.txt']

# The folder is C:\delicious\breakfastFavorites\sandwiches
# The subfolders in C:\delicious\breakfastFavorites\sandwichesare[]
# The files in C:\delicious\breakfastFavorites\sandwichesare['englishMuffinAndSauagePattyAndCheese.txt']

# The folder is C:\delicious\tastyFood
# The subfolders in C:\delicious\tastyFoodare[]
# The files in C:\delicious\tastyFoodare['favoriteFoods.txt']

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + 'are' + str(subfolders))
    print('The files in ' + folderName + 'are' + str(filenames))
    print()
    
    for subfolder in subfolders:
        # you could have code that deletes the subfolder:
        # os.unlink(subfolder)
        # Or specify if a folder name exists, delete 
        # that one 
        if 'fish' in subfolder:
            os.rmdir(subfolder)
        print(subfolder)
    for file in filenames:
        if file.endswith('.rb'):
            shutil.copy( \
                os.path.join(folderName, file), \
                os.path.join(folderName, file + '.backup'))
            
# REMEMBER, os.walk has a return value that is used 
# in a for loop, which in turn returns three values 
# in each iteration: foldername, subfolders, file