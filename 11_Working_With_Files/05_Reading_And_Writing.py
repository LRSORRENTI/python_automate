# Reading and writing to plaintext files 

# Plaintext files don't include any fontsize, text 
# color or any specifications, just text, usually
# appended with .txt 

# The first step to readig and writing to files is 
# the open() function 

# open('C:\\Users\\lrsor\\test.txt')

# The open function by default only let's you read 
# the file, you can't modify or add to it with open

# The open call returns a file object, so save it 
# to a variable 

fileObj = open('C:\\Users\\lrsor\\test.txt')
# print(fileObj.read())
# the read() method will log the text inside the 
# file:

# Hello there, 
# how are you?

# Save the fileObj.read to it's own variable:

content = fileObj.readlines()
# print(content)
# Hello there, 
# how are you?


# Reset the pointer to the start of the file if you want to read again
fileObj.seek(0)

# there's also the readlines method for file objects:
print(fileObj.readlines())
# ['Hello there, \n', 'how are you?\n']
myArr = []
myArr.insert(0, content)
print(myArr)
# [['Hello there, \n', 'how are you?\n']]
fileObj.close()

# That's it for reading from files for now, let's go 
# over how to modify and write to a file