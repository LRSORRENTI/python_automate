# Another example of how try and except blocks 
# are crucial in python

# Suppose you're writing a program that reads data 
# from a file and processes it. However, 
# if the file is not found or there's an 
# error reading from it, the program will crash. 

# To avoid this, you can use a try except block to
# handle the error and provide a graceful way to 
# handle the situation.
import os

def read_data_from_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Error reading from file {filename}: {e}")

    return None  # Explicitly return None if an exception occurred

# In this example, the `read_data_from_file()` 
# function tries to open a file and read data from it.

# If the file is not found, a `FileNotFoundError` 
# exception is thrown, which is caught by the except 
# statement and an error message is printed.

# If there's any other error reading from the file, 
# such as a syntax error or a permissions error, the 
# `Exception` catch-all block catches it and prints an 
# error message with the details of the exception.
# By using the try except block, the program can 
# continue to run safely and prevent unexpected 
# errors from occurring, making it more robust and 
# reliable.