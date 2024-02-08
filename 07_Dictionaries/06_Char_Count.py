# Write a program that will count the amount 
# of characters in a string 

message = 'It was a bright cold day in April, \
    and the clocks were striking thirteen'

count = {}

for char in message.upper():
    count.setdefault(char, 0)
    # setdefault is important, since the first time
    # we try to increment a key that doesn't exist,
    # it will cause an error
    count[char] = count[char] + 1

print(count)

# {'I': 7, 'T': 6, ' ': 17, 'W': 2, 'A': 5,
# 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3,
# 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 
# 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2}

