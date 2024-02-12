# rjust and ljust methods:

str = 'hello'
print(str.rjust(10))
#      hello
str2 = 'hi there'
print(str2.ljust(10, '*'))
# hi there**

# center method 
print(str.center(20, '='))
# =======hello========

# replace method will take a first argument of a 
# specified str and replace that with the second 
# argument
print(str.replace('e', 'XYZ'))
# hXYZllo