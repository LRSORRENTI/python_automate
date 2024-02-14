# REGEX Groups and the Pipe character
import re 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObj = phoneNumRegex.search('My number is 444-555-2231')
print(matchObj.group())
# 444-555-2231

# The above returns the full phone number, but say 
# we wanted to just return the area code, we can do 
# this by using groups, or sets or parentheses around 
# the sections we need

phoneNumRegexTwo = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObjTwo = phoneNumRegexTwo.search('My number is 444-555-2231')

# Then you specify the group number like below:
print('Matchobj group 1: ', matchObjTwo.group(1), 
      'Matchobj group 2: ',matchObjTwo.group(2))

# Matchobj group 1:  444 Matchobj group 2:  555-2231
# Also note if you need to search for parentheses 
# themselves, you'll need to use an escape character

# PIPE CHARACTERS | 

# The pipe character is used when you'd want to 
# specify multiple strings or patterns to find at 
# the same time

# We want to search for light, and all suffixes for 
# light, we wrap parentheses and use pipe char to 
# separate
# lightRegex = re.compile(r'light(bulb)|(ning)|(room)|(wood)')
# light = 'the lightning was visible, the lightbulb \
#          flashed in the lightroom, which walls are \
#          made of lightwood'
# mo = lightRegex.search(light)
# print(mo.group(1))

lightRegex = re.compile(r'\b(light\w*)\b')
light = 'the lightning was visible, the lightbulb \
         flashed in the lightroom, which walls are \
         made of lightwood'

matches = lightRegex.findall(light)

for match in matches:
    print(match)
# lightning
# lightbulb
# lightroom
# lightwood
