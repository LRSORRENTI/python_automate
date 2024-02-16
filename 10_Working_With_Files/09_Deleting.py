# To delete files and folders you can use the 
# os.unlink method will delete a specified file path

import os 
import shutil
# os.unlink('C:\\Users\\lrsor\\Desktop\\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\testDEL.txt')
# after execution, python will indeed delete the 
# testDEL.txt file 

# To delete entire folders, use the rmdir method:

# os.rmdir('C:\\Users\\lrsor\\Desktop\\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\testRMDIR')
# Note, rmdir only works on empty folders, if a folder 
# has files within it, directly calling rmdir will 
# not work

# But if you do wish to delete an entire folder and 
# all of it's content, use shutil.rmtree()

# shutil.rmtree('C:\\Users\\lrsor\\Desktop\\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\testRMDIR2')

# NOTE These will completely erase the folder / file and all of it's contents permanently

# NOTE To use a safer way to delete files and folders,
# the send2trash method is the way, this is not built 
# into python, you'll need to use pip install send2trash 

import send2trash
send2trash.send2trash('C:\\Users\\lrsor\\Desktop\\CURRENT-PROJECTS\\automate_python\\10_Working_With_Files\\testsend2trash.txt')