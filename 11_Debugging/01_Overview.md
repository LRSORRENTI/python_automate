# Debugging Python

Often when building programs, bugs appear, some simpler, some more complex, the next few lessons will go over how to process and find the root cause of any given bug in your program

We've learned about try and except statements to calibrate for errors that are likely to occur, so the program can recover from them

But we can raise our own exceptions, these are used with a 'raise' statement

Then you call the Exception function:

```
raise Exception('This is the error message!!')
```
