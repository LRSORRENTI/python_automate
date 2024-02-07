# looping lists 

for i in range (4): 
    print(0, 1, 2, 3)
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3

for i in [0, 1, 2, 3]:
    print(i)
# 0
# 1
# 2
# 3

snakes = ['Boa', 'Anaconda', 'Viper', 'Cobra', 'Python']
for i in snakes:
    print(i)
# Boa
# Anaconda
# Viper
# Cobra
# Python
    
# You can also pass in the range function as an 
# argument to list if you need to quickly return 
# an array of numbers
    
print(list(range(11)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numList = list(range(0, 50, 2))
print(numList)

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
# 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

fishingSupplies = ['Rods', 'Reels', 'Tackle', 'Bait']
for i in range(len(fishingSupplies)):
    print('Index ' + str(i) + ' in fishing supplies is ' + fishingSupplies[i])

# Index 0 in fishing supplies is Rods
# Index 1 in fishing supplies is Reels
# Index 2 in fishing supplies is Tackle
# Index 3 in fishing supplies is Bait


