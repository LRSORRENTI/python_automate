# Multiple Assignment in Python 

# Python has a multiple assignment trick to quickly 
# assign list values to variables:
cats = ['Tabby', 'Scottish Fold', 'Bengal', 'Sphinx']

# assign values from a list quickly with: 
tabby, scottishFold, bengal, sphinx = cats 
print(tabby, scottishFold, bengal, sphinx)
# Tabby Scottish Fold Bengal Sphinx
print(sphinx, tabby) 
# Sphinx, Tabby

# This multiple assignment method is often used 
# to perform swap operations to swap variables quickly

name, age, hobby = 'Pete', '22', 'Wakeboarding'
print(name, age, hobby)
# Pete 22 Wakeboarding

# And you can quickly reassign like: 
name, age = hobby, name
print(name, age)
# Wakeboarding Pete

# Augment Assignment Operators: 

# Take the variable below: 

num = 10
num = num + 1
print(num)
# 11

# the above could be also achieved with: 

numb = 10
numb += 1
print(numb)
# 11

# All of the operators are availble:

numOne = 20
print(numOne) # 20
numOne += 1 
print(numOne) # 21
numOne -= 1 
print(numOne) # 20
numOne /= 5
print(numOne) # 4.0
numOne %= 0.1
print(numOne) # 0.09999999999999978