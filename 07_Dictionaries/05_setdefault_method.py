fish = {
    'fish1': 'Pike',
    'fish2': 'Bass',
    'fish3': 'Perch',
    'fish4': 'Bluegill',
    'fish5': 'Muskellunge'
}

if 'fish6' not in fish:
    fish['fish6'] = 'Carp'
print(fish)

# setdefault exposes an easier way of 
# achieving the same as if not in 

fish.setdefault('fish7', 'Sturgeon')
print(fish)
# {'fish1': 'Pike', 'fish2': 'Bass',
# 'fish3': 'Perch', 'fish4': 'Bluegill',
# 'fish5': 'Muskellunge', 'fish6': 'Carp',
# 'fish7': 'Sturgeon'}  