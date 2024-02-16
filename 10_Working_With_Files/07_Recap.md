# Recap

- open() method returns a file object which has reading and writing related methods

- Pass 'r' (or nothing) to open the file in read-mode, 'w' to use write-mode, and 'a' to use append-mode

- Opening a nonexistant file name in write or append mode will create a file with that passed in name

- Call read() or write() to read the contents of a file, or write a string to the file

- Call readlines() to return a list of strings containing the files content

- Call close() when you're finished working with the file

- Use shelve module when needing to use a dictionary like structure for data

- shelve module stores python values in binary file format
