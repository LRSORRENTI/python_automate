# Copying and moving files in python 

# If you ever need to copy, organize or rename 
# hundreds or thousands of folders and files by hand 

# Use python instead to automate the process using 
# the shutil module 

import shutil
shutil.copy('C:\\Users\\lrsor\\test2.txt',
            'C:\\Users\\lrsor\\Desktop\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\' )
# After executing the above, the file is indeed 
# inside this directory, copied from it's orginal 
# file location

# You can also rename the file by passing in a new 
# name in the second argument: 

shutil.copy('C:\\Users\\lrsor\\test.txt',
            'C:\\Users\\lrsor\\Desktop\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\renamed.txt' )

# You can also use shutil to copy entire folders using:

shutil.copytree('C:\\Users\\lrsor\\testingSHUTIL_COPYTREE' ,'C:\\Users\\lrsor\\testingSHUTIL_COPYTREE_Copy')
# The above copied the folder and saved it as a new 
# folder in the same directory as it's original

