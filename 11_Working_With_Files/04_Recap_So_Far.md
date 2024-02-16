# Recap

- All files have a name and a path

- The root folder is the lowest folder, it's C:\ on windows and / on Linux & Mac

- Ina file path, the folders and filename are separated by backslashes on windows, and forward slashes on Linux and Mac

- Use the os.path.join() function to combine folders with the correct slash

- The current working directory is the folder that any relative paths are relative to

- os.getcwd() returns the current working directory

- os.chdir() changes the current working directory

- Absolute paths begin with the root folder, relative paths do not

- The . folder represents 'the folder', while .. folder represents the parent folder

- os.path.abspath() returns the absolute path form of the path passed to it

- os.path.isabs() returns True if the path passed to it is absolute

- os.path.relpath() returns the relative path between two paths passed to it

- os.makedirs() can make folders

- os.path.getsize() returns a file's size

- os.listdir() returns a list of strings of filenames

- os.path.exists() returns True if the filename passed to it exists

- os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path
