# os module 

# Ideally we'd like to write python that's
# usable across operating systems, we can 
# use the os module to help with this 

import os 

testPath = os.path.join('folder1', 'folder2', 'folder3', 'file.txt')
print(testPath)
# folder1\folder2\folder3\file.txt

# If we were on a linux or mac the output would be
# forward slashes:

# folder1/folder2/folder3/file.txt

print(os.getcwd())

# C:\Users\user1\Desktop\CURRENT-PROJECTS\automate_python\10_Working_With_Files\

# You can also change current working directory with:

# os.chdir('c:\\')