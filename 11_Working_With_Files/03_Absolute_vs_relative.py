# Absolute and relative paths are two ways to 
# point to a file

# Absolute file paths begin with 
# 'c:\\folder\folder2\folder3\script.py'

# Relative file paths are relative to the current 
# directory

# 11_Working_With_Files\03_Absolute_vs_relative.py

import os 

# os.chdir('c:\\folder\\folder2\\folder3\\script.py')

print(os.path.abspath('script.py'))
# c:\\folder\\folder2\\folder3\\script.py
# print(os.path.abspath('..\..\script.py'))

# you can also check is a path is absolute with:
print(os.path.isabs('C:\\Users\\user1\\Desktop\\CURRENT-PROJECTS\\automate_python\\11_Working_With_Files\\03_Absolute_vs_relative.py'))
# True

# relpath()

# the relpath method takes two arguments, and will return 
# the correct pathway between them

print(os.path.relpath('C:\\Users\\user1\\Desktop\CURRENT-PROJECTS\\automate_python\\11_Working_With_Files\\03_Absolute_vs_relative.py',
                       'C:\\Users\\user1\\Desktop\\Programming\\weather-app\\src\\api\\weather.ts' ))
# ..\..\..\..\..\CURRENT-PROJECTS\automate_python\11_Working_With_Files\03_Absolute_vs_relative.py

# os.path.dirname('C:\\folder1\\folder2\\spam.png')
# 'c:\folder1\folder2'

# os.path.basename()
# 'spam.png'

# os.path.exists() 
# this will check if a given fle path exists, and 
# returns a boolean

# other boolean file checks include:
# os.path.isfile()
# and 
# os.path.isdir()

# the os.path.getsize() will return an integer 
# of bytes 

# print(os.path.getsize('C:\\Users\\user1\\Desktop\CURRENT-PROJECTS\\automate_python\\11_Working_With_Files\\03_Absolute_vs_relative.py'))
# 1619

# print(os.listdir('C:\\Users\\user1\\Desktop\CURRENT-PROJECTS\\automate_python\\'))
# ['.git', '.gitignore', '.venv', '01_Python_Basics',
#   '02_Flow_Control', '03_Functions',
#   '04_Try_Except_Statements', '05_Guess_Number',
#   '06_Lists', '07_Dictionaries',
#   '08_Advanced_String_Methods', '09_REGEX',
#   '11_Working_With_Files', 'myenv',
#   'NOTE_ABOUT_MYENV.md', 'requirements.txt']

totalSize = 0
for filename in os.listdir('C:\\Users\\user1\\Desktop\CURRENT-PROJECTS\\automate_python\\'):
    if not os.path.isfile(os.path.join('C:\\Users\\user1\\Desktop\CURRENT-PROJECTS\\automate_python\\', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\lrsor\\Desktop\CURRENT-PROJECTS\\automate_python\\', filename))
    print(totalSize)
                      