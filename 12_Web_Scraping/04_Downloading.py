# Downloading with the requests module 

import requests

# we can use .get to get the data, and it returns a 
# response objecT:

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# call raise for status to raise an exception if there 
# was an error downloading the file, and will do nothing
# if the download is successful
print(res.raise_for_status())
res.raise_for_status()

# We can test a bad url to see the negative: 
# res = requests.get('https://automatetheboringstuff.com/files/rj22222.txt')

# raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://automatetheboringstuff.com/files/rj22222.txt


print(res.status_code)
# 200

print(len(res.text))
# 178978

print(res.text[:500])
# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

# This eBook is for the use of anyone anywhere at no cost and with  
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.org/license


# Title: Romeo and Juliet

# Author: William Shakespeare

# Posting Date: May 25, 2012 [EBook #1112]
# Release Date: November, 1997  [Etext #1112]

# Language: Eng

# Instead of printing, let's save it to a file, 
# you need to pass 'wb' as an argument to write 
# to it:

playFile = open('RomeoAndJuliet.txt', 'wb')

# And we use a for loop, and the res objects 
# inner contnet method 

for chunk in res.iter_content(100000):
    # Each chunk is of the bytes data type,
    # above we pass 100000 for that number of 
    # bytes per iteration of the loop
    playFile.write(chunk)

playFile.close()