# Recap

- os.unlink() will delete a file

- os.rmdir() will delete an empty folder

- shutil.rmtree() will delete a folder and all of it's files / folders nested within

- Deleting using the above methods are unrecoverable, to send deletions to trash use the send2trash python package, and the send2trash method for a safer alternative
