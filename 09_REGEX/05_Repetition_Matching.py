# Repetition Matching

# You may want to match a certain number or 
# repetitions of a group 

import re 

# Use the '?' to specify that the pattern can appear
# 0 or 1 time
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())
# Batman
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())
# Batwoman
